# Notes de mise à jour - Compatibilité Python 3.14

## Problèmes rencontrés

1. **Versions de packages incompatibles**: Les versions strictes (`==`) n'étaient pas disponibles pour Python 3.14
2. **Pydantic V1**: LangChain utilise encore Pydantic V1 qui n'est pas officiellement compatible avec Python 3.14
3. **Modules réorganisés**: LangChain a changé sa structure dans les versions 0.3+

## Solutions appliquées

### 1. Requirements mis à jour
- Utilisation de versions flexibles (`>=`) au lieu de strictes
- Ajout de `langchain-community` pour les composants manquants
- Upgrade vers LangChain 0.3+ pour meilleure compatibilité

### 2. Code modernisé avec LCEL
Remplacement de l'ancienne API `RetrievalQA` par la nouvelle LCEL (LangChain Expression Language):

**Ancien code**:
```python
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)
result = qa_chain.invoke({"query": question})
```

**Nouveau code**:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

template = """..."""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
answer = rag_chain.invoke(question)
```

### 3. Imports corrigés
- `langchain.text_splitter` → `langchain_text_splitters`
- `langchain.schema` → `langchain_core.documents`
- `langchain.chains` → composants LCEL de `langchain_core`

## Avantages de LCEL

1. **Plus moderne**: API recommandée par LangChain
2. **Plus flexible**: Composition facile de chaînes complexes
3. **Meilleure compatibilité**: Fonctionne avec Python 3.14
4. **Plus performant**: Meilleure gestion du streaming

## Avertissements à ignorer

```
UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
```

Ce warning peut être ignoré, le code fonctionne correctement malgré l'avertissement.

## Alternative recommandée

Pour un environnement de production, il est recommandé d'utiliser **Python 3.12** qui est mieux supporté par l'écosystème LangChain actuel. Python 3.14 est très récent et certaines librairies n'ont pas encore été mises à jour.
