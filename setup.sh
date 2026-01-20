#!/bin/bash

echo "Installation des dépendances..."
pip install -r requirements.txt

echo "Configuration du kernel Jupyter..."
python -m ipykernel install --user --name=rag-venv --display-name="Python (RAG)"

echo ""
echo "✓ Installation terminée!"
echo ""
echo "Pour utiliser le notebook:"
echo "1. Lancez: jupyter notebook rag_notebook.ipynb"
echo "2. Dans le menu: Kernel > Change Kernel > Python (RAG)"
echo ""
