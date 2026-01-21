# RAG Basique - Qdrant + Mistral

Système RAG (Retrieval-Augmented Generation) minimaliste pour interroger des documents.

## Formats supportés
- CSV
- TXT
- JSON
- PDF

## Installation

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances et configurer Jupyter
bash setup.sh

# OU manuellement:
pip install -r requirements.txt
python -m ipykernel install --user --name=rag-venv --display-name="Python (RAG)"
```

## Configuration

rentrer vos clés API dans un fichier `.env` (cf fichier env.example).

**Note**: Vous verrez un avertissement sur Pydantic V1 avec Python 3.14, c'est normal et peut être ignoré. Le code fonctionne malgré cet avertissement.

## Utilisation

### Option 1: Jupyter Notebook

```bash
jupyter-notebook rag_notebook.ipynb
```

**Important**: Sélectionnez le kernel "Python (RAG)" dans le menu `Kernel > Change Kernel`

Exécutez les cellules dans l'ordre:
1. Configuration et imports
2. Initialisation des composants
3. Chargement des documents depuis `data/`
4. Indexation dans Qdrant
5. Interrogation du système

### Option 2: Interface Streamlit

```bash
streamlit run app.py
```

L'interface s'ouvre dans votre navigateur. Posez vos questions directement.

## Ajout de documents

Placez vos fichiers dans le dossier `data/`:
Le système charge automatiquement tous les fichiers supportés.

## Architecture

- **LLM**: Mistral (mistral-small-latest)
- **Embeddings**: Mistral (mistral-embed)
- **Vector Store**: Qdrant (cloud)
- **Orchestrateur**: LangChain
- **Interface**: Streamlit / Jupyter

## Principe de fonctionnement

1. Les documents sont chargés et découpés en chunks
2. Chaque chunk est transformé en embedding
3. Les embeddings sont stockés dans Qdrant
4. À la question de l'utilisateur:
   - Le système trouve les chunks pertinents
   - Le LLM génère une réponse basée uniquement sur ces chunks
   - Les sources sont affichées
