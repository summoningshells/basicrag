import os
import json
import csv
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from qdrant_client import QdrantClient

from pypdf import PdfReader

# Configuration
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
QDRANT_ENDPOINT = os.getenv("QDRANT_ENDPOINT")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "documents_rag"

# Fonctions de chargement
def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return [Document(page_content=content, metadata={"source": file_path, "type": "txt"})]

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    content = json.dumps(data, indent=2, ensure_ascii=False)
    return [Document(page_content=content, metadata={"source": file_path, "type": "json"})]

def load_csv(file_path):
    documents = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            content = "\n".join([f"{k}: {v}" for k, v in row.items()])
            documents.append(
                Document(page_content=content, metadata={"source": file_path, "type": "csv", "row": i})
            )
    return documents

def load_pdf(file_path):
    reader = PdfReader(file_path)
    documents = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text.strip():
            documents.append(
                Document(page_content=text, metadata={"source": file_path, "type": "pdf", "page": i})
            )
    return documents

def load_documents_from_directory(directory):
    all_documents = []
    data_path = Path(directory)

    if not data_path.exists():
        return all_documents

    loaders = {
        '.txt': load_txt,
        '.json': load_json,
        '.csv': load_csv,
        '.pdf': load_pdf
    }

    for file_path in data_path.rglob('*'):
        if file_path.is_file():
            ext = file_path.suffix.lower()
            if ext in loaders:
                try:
                    docs = loaders[ext](str(file_path))
                    all_documents.extend(docs)
                except Exception as e:
                    st.warning(f"Erreur lors du chargement de {file_path.name}: {e}")

    return all_documents

# Initialisation du cache Streamlit
@st.cache_resource
def init_components():
    qdrant_client = QdrantClient(
        url=QDRANT_ENDPOINT,
        api_key=QDRANT_API_KEY
    )

    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        mistral_api_key=MISTRAL_API_KEY
    )

    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=MISTRAL_API_KEY,
        temperature=0
    )

    return qdrant_client, embeddings, llm

@st.cache_data
def load_and_index_documents(_qdrant_client, _embeddings):
    documents = load_documents_from_directory("data")

    if not documents:
        return None, 0

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(documents)

    # Supprimer la collection si elle existe
    try:
        _qdrant_client.delete_collection(COLLECTION_NAME)
    except:
        pass

    # Créer le vector store
    vector_store = QdrantVectorStore.from_documents(
        splits,
        _embeddings,
        url=QDRANT_ENDPOINT,
        api_key=QDRANT_API_KEY,
        collection_name=COLLECTION_NAME
    )

    return vector_store, len(splits)

# Interface Streamlit
def main():
    st.title("RAG - Interrogation de Documents")
    st.markdown("Posez des questions sur vos documents (CSV, TXT, JSON, PDF)")

    # Initialisation
    qdrant_client, embeddings, llm = init_components()

    # Sidebar
    with st.sidebar:
        st.header("Configuration")
        st.info("Documents chargés depuis le dossier 'data/'")

        if st.button("Recharger les documents"):
            st.cache_data.clear()
            st.rerun()

    # Chargement et indexation
    with st.spinner("Chargement et indexation des documents..."):
        vector_store, num_chunks = load_and_index_documents(qdrant_client, embeddings)

    if vector_store is None:
        st.warning("Aucun document trouvé dans le dossier 'data/'. Ajoutez des fichiers et rechargez.")
        st.info("Formats supportés: .txt, .json, .csv, .pdf")
        return

    st.success(f"{num_chunks} chunks indexés")

    # Zone de question
    question = st.text_input("Votre question:", placeholder="Ex: Résume les informations principales")

    if question:
        with st.spinner("Recherche de la réponse..."):
            retriever = vector_store.as_retriever(search_kwargs={"k": 3})

            # Template pour le prompt RAG
            template = """Tu dois répondre UNIQUEMENT à partir des informations fournies dans le CONTEXTE ci-dessous.
Si une information n'est pas présente dans le CONTEXTE, dis clairement que tu ne sais pas.
Ne fabrique pas de réponses.

CONTEXTE:
{context}

QUESTION: {question}

RÉPONSE:"""

            prompt = ChatPromptTemplate.from_template(template)

            # Créer la chaîne RAG avec LCEL
            def format_docs(docs):
                return "\n\n".join([doc.page_content for doc in docs])

            rag_chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )

            # Récupérer les sources et la réponse
            source_docs = retriever.invoke(question)
            answer = rag_chain.invoke(question)

        # Affichage de la réponse
        st.markdown("### Réponse")
        st.write(answer)

        # Affichage des sources
        with st.expander("Sources utilisées"):
            for i, doc in enumerate(source_docs, 1):
                st.markdown(f"**Source {i}:** {doc.metadata.get('source', 'N/A')} (type: {doc.metadata.get('type', 'N/A')})")
                st.text(doc.page_content[:300] + "...")
                st.divider()

if __name__ == "__main__":
    main()
