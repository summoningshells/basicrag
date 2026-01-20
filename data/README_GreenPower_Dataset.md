# GreenPower Solutions - Fake Data Package
## Formation AI4Industry - Dataset Complet

**Date de création :** 6 janvier 2026  
**Société fictive :** GreenPower Solutions (basée sur Ecologene)  
**Objectif :** Formation ingénieurs sur RAG et GraphRAG avec Mensaflow

---

## 📦 Contenu du Package

### 1. **greenpower_products.json** (12 KB)
**Format :** JSON structuré  
**Contenu :** 
- 5 modèles de produits (PG-U01 à PG-M02)
- Spécifications techniques complètes
- Prix, garanties, cas d'usage
- 4 accessoires complémentaires
- 3 services professionnels

**Utilisation :**
```bash
# Charger dans un RAG vectoriel
python load_documents.py --file greenpower_products.json --type json

# Pour GraphRAG, extraire les relations :
# - Produit → cas d'usage
# - Produit → accessoire compatible
# - Produit → documentation associée
```

**Clés importantes :**
- `product_id` : Identifiant unique (PG-U01, PG-M01, etc.)
- `use_cases[]` : Liste des applications (important pour requêtes sémantiques)
- `related_docs[]` : Sources croisées pour le chatbot

---

### 2. **greenpower_qa_dataset.csv** (15 KB)
**Format :** CSV (UTF-8)  
**Contenu :** 30 paires Question/Réponse avec sources croisées

**Structure :**
```csv
Question_ID,Question,Answer,Source_References
Q001,"What is...","The GreenPower...","[Source: greenpower.com/...] [Document: ...]"
```

**Colonnes :**
- `Question_ID` : Q001 à Q030 (identifiant unique)
- `Question` : Question client en anglais (naturelle, variée)
- `Answer` : Réponse détaillée avec contexte
- `Source_References` : Sources web + documents internes

**Utilisation pour la formation :**
1. **Test RAG simple** : Recherche vectorielle des questions similaires
2. **Test GraphRAG** : Suivre les références croisées entre documents
3. **Benchmark** : Mesurer précision et temps de réponse

**Exemple de test :**
```python
# Question test : "Can I rent a system for a festival?"
# RAG devrait retourner : Q002 (high similarity)
# GraphRAG devrait aussi lier : Q001 (specifications), Q011 (events powered)
```

---

### 3. **greenpower_events.json** (16 KB)
**Format :** JSON structuré  
**Contenu :**
- 4 salons/expositions (trade shows)
- 6 événements alimentés (festivals, construction)
- 2 déploiements construction longue durée
- 3 couvertures médiatiques
- Statistiques globales

**Utilisation GraphRAG :**
Les événements créent des **relations temporelles et géographiques** :
```
GreenSound Festival → utilise → PG-U01 (x2) + PG-M01 (x4)
                   → économise → 8,500L diesel
                   → évite → 22.7 tonnes CO2
                   → lieu → Bordeaux
                   → date → Sept 2025
```

**Requêtes GraphRAG avancées :**
- "Quels événements ont utilisé le PG-M01 ?"
- "Combien de CO2 économisé sur tous les festivals en 2024-2025 ?"
- "Où GreenPower a-t-il été déployé dans le Sud de la France ?"

---

### 4. **greenpower_technical_docs.md** (47 KB)
**Format :** Markdown (10 sections complètes)  
**Contenu :**
- Documentation technique exhaustive (70+ pages équivalent)
- Spécifications produits détaillées
- Guides installation, maintenance, dépannage
- Codes d'erreur, safety, compliance
- Exemples de calculs et cas d'usage

**Structure :**
1. Company Overview
2. Technology Foundation
3. Product Line Specifications (5 modèles détaillés)
4. Installation Guidelines
5. Operation & Maintenance
6. Troubleshooting Guide (codes erreur E01-E14)
7. Safety & Compliance
8. Performance Optimization
9. Technical Support
10. Appendices (glossaire, câblage, calculs)

**Utilisation :**
- **RAG vectoriel** : Chunking par sections (headers H2/H3)
- **GraphRAG** : Extraire relations entre :
  - Problème (code erreur) → Solution
  - Modèle → Spécifications techniques
  - Accessoire → Modèles compatibles
  - Document → Document connexe

**Exemple de requête complexe :**
```
Q: "Mon système PG-M01 affiche l'erreur E04, que faire ?"

RAG simple : Trouve section "6.2 Error Codes" → E04 = Cell Voltage Imbalance

GraphRAG : 
- E04 → "Allow BMS balancing cycle"
- BMS → Section "2.2.1 Battery Management System"
- E04 persist >48h → "contact support" → Section "9.1 Support Tiers"
- Related: E02 (Battery Temperature High) peut causer E04
```

---

## 🎯 Utilisation pour la Formation AI4Industry

### Partie 1 : RAG vs GraphRAG

#### Démo RAG Traditionnel
```bash
# 1. Charger les données dans une base vectorielle (ChromaDB, Pinecone, etc.)
python scripts/load_to_vectordb.py \
  --products greenpower_products.json \
  --qa greenpower_qa_dataset.csv \
  --docs greenpower_technical_docs.md

# 2. Test de requête
query = "What is the battery capacity of the Max model?"
# RAG retourne : Section du JSON ou QA-Q001
```

**Limitation RAG :** 
- Trouve "Max model" et "battery capacity" sémantiquement
- Mais ne comprend pas les relations : PG-M01 → compatible avec → PG-ACC-02 (Battery Expansion)

---

#### Démo GraphRAG
```bash
# 1. Extraire les entités et relations
python scripts/build_knowledge_graph.py \
  --input greenpower_*.json greenpower_technical_docs.md \
  --output greenpower_graph.db

# 2. Créer le graphe de connaissances (Neo4j)
# Nodes: Products, Events, Documents, Specs, Locations
# Edges: uses, compatible_with, references, located_in, happened_at

# 3. Test requête complexe
query = "Which events in 2024 used systems with battery capacity > 500 kWh?"
# GraphRAG peut naviguer :
# Events → uses → Products → has_spec → Battery Capacity → filter > 500kWh
```

**Avantage GraphRAG :**
- Comprend les relations multi-hop
- Réponses plus contextuelles et précises

---

### Partie 2 : Dashboard de Performance

#### Métriques à Mesurer

**Pour chaque système (RAG vs GraphRAG) :**

1. **Vitesse d'inférence**
   - Temps de recherche (ms)
   - Temps de génération réponse (ms)
   - Temps total (ms)

2. **Qualité de réponse**
   - Précision (réponse correcte ?)
   - Complétude (toutes les infos pertinentes ?)
   - Sources citées (bonnes références ?)

3. **Taux d'hallucination**
   - Infos inventées
   - Dates/chiffres incorrects
   - Sources inexistantes

**Dataset de test recommandé :**
```python
test_questions = [
    # Questions simples (RAG devrait bien réussir)
    "What is the price of PG-C01?",
    "How long does installation take?",
    
    # Questions avec relations (GraphRAG supérieur)
    "Which systems were used at festivals in France in 2024?",
    "What accessories are compatible with hybrid mode?",
    
    # Questions complexes multi-hop
    "If I have error E04 on a PG-M01, what related problems should I check for?",
    "What's the total CO2 savings from all events using PG-M01 in 2024-2025?"
]
```

---

### Code Exemple : Dashboard Comparaison

```python
import streamlit as st
import time

# Test query
query = "What events used the Max model?"

# RAG Simple
start_rag = time.time()
rag_response = rag_system.query(query)
rag_time = time.time() - start_rag

# GraphRAG
start_graph = time.time()
graph_response = graph_rag_system.query(query)
graph_time = time.time() - start_graph

# Dashboard
st.title("RAG vs GraphRAG Comparison")

col1, col2 = st.columns(2)

with col1:
    st.header("RAG Traditional")
    st.metric("Response Time", f"{rag_time*1000:.0f} ms")
    st.write(rag_response)

with col2:
    st.header("Graph RAG")
    st.metric("Response Time", f"{graph_time*1000:.0f} ms")
    st.write(graph_response)
    
    # Show knowledge path
    st.subheader("Knowledge Graph Path")
    st.graphviz_chart(graph_rag_system.get_reasoning_path())
```

---

## 🔗 Relations Clés dans le Dataset

Pour GraphRAG, voici les relations importantes à extraire :

### Relations Produits
```
PG-M01 (Max)
  ├── has_capacity → 180 kVA
  ├── has_battery → 720 kWh
  ├── uses_battery_type → "Second-life Tesla batteries"
  ├── compatible_with → PG-ACC-01 (Solar Array)
  ├── compatible_with → PG-ACC-02 (Battery Expansion)
  ├── compatible_with → PG-ACC-03 (Hybrid Kit)
  ├── used_at → GreenSound Festival
  ├── used_at → Terres du Rhythm Festival
  ├── used_at → Highway A9 Valmanya
  └── documented_in → Manual_PG-M01_v3.2.pdf
```

### Relations Événements
```
GreenSound Festival
  ├── located_in → Bordeaux
  ├── happened_on → September 2025
  ├── powered_by → PG-U01 (x2)
  ├── powered_by → PG-M01 (x4)
  ├── saved_fuel → 8,500 liters
  ├── avoided_co2 → 22.7 tonnes
  ├── had_attendees → 42,000 people
  └── documented_in → Case_Study_GreenSound_2025.pdf
```

### Relations Techniques (Troubleshooting)
```
Error_E04
  ├── severity → "Alarm"
  ├── meaning → "Cell Voltage Imbalance"
  ├── solution → "Allow BMS balancing cycle"
  ├── related_to → BMS (Battery Management System)
  ├── may_be_caused_by → Error_E02 (High Temperature)
  └── if_persists → "contact technical support"
```

---

## 📊 Statistiques du Dataset

**Produits :** 5 modèles + 4 accessoires = 9 entités produits  
**Questions/Réponses :** 30 paires (couvrant specs, pricing, usage, support)  
**Événements :** 4 salons + 6 événements alimentés + 2 projets construction = 12 déploiements  
**Documents techniques :** 1 guide complet (10 sections, ~15,000 mots)  
**Sources fictives :** ~45 documents référencés (PDFs, guides, rapports)  

**Relations potentielles pour GraphRAG :** ~200+ edges

**Complexité linguistique :**
- Anglais technique professionnel
- Vocabulaire spécialisé énergie/électricité
- Acronymes industriels (kVA, kWh, BMS, MPPT, etc.)

---

## 🚀 Instructions de Déploiement Formation

### Étape 1 : Préparation Serveur
```bash
# Sur server00
cd /opt/mensaflow/training/ai4industry

# Copier les fake data
scp greenpower_*.* user@server00:/opt/mensaflow/data/greenpower/

# Créer les espaces élèves (exemple pour 20 élèves)
for i in {1..20}; do
    mkdir -p /opt/mensaflow/students/student_$i/greenpower
    cp greenpower_*.* /opt/mensaflow/students/student_$i/greenpower/
done
```

### Étape 2 : Configuration RAG
```bash
# Initialiser la base vectorielle
python scripts/init_vectordb.py \
  --name greenpower_rag \
  --data /opt/mensaflow/data/greenpower/ \
  --embeddings sentence-transformers/all-MiniLM-L6-v2

# Vérifier l'indexation
python scripts/verify_indexing.py --db greenpower_rag
# Expected: ~150 documents indexés
```

### Étape 3 : Configuration GraphRAG (LightRAG)
```bash
# Créer le knowledge graph
python scripts/build_graph.py \
  --input /opt/mensaflow/data/greenpower/ \
  --neo4j bolt://server00:7687 \
  --database greenpower_graph

# Vérifier le graphe
cypher "MATCH (n) RETURN count(n)"
# Expected: ~80-100 nodes

cypher "MATCH ()-[r]->() RETURN count(r)"
# Expected: ~200-250 relationships
```

### Étape 4 : Lancer le Chatbot Demo
```bash
# Terminal 1 : API Backend
cd /opt/mensaflow/api
uvicorn main:app --host 0.0.0.0 --port 8000

# Terminal 2 : Frontend Dashboard
cd /opt/mensaflow/dashboard
streamlit run compare_rag.py --server.port 8501
```

**Accès :**
- Chatbot : http://server00:8501
- API docs : http://server00:8000/docs

---

## 📝 Questions Test Suggérées (30 Questions)

### Niveau 1 : Questions Simples (RAG Traditionnel OK)
1. What is the battery capacity of the PG-M01?
2. How much does the Compact model weigh?
3. What is the warranty period for solar panels?
4. Can I rent a GreenPower system?
5. What is the noise level of the Mini model?

### Niveau 2 : Questions avec Contexte (GraphRAG commence à briller)
6. Which models are compatible with the Hybrid Diesel Interface Kit?
7. What events in France used GreenPower systems in 2024?
8. How much CO2 was saved at the GreenSound Festival?
9. What accessories can I add to the Performance model?
10. Which systems support three-phase power output?

### Niveau 3 : Questions Multi-Hop (GraphRAG supérieur)
11. If I have a construction site in Paris ZFE, which model should I choose and why?
12. What's the total fuel saved across all events in 2024-2025?
13. Show me all festivals that used systems with >500 kWh battery capacity.
14. If error E04 appears on my system, what related errors should I check for?
15. Which events happened in Southern France and what equipment did they use?

### Niveau 4 : Questions Complexes (Test Raisonnement)
16. I need to power a 3-day festival with 50,000 attendees. Design a system for me.
17. Compare the ROI between PG-M01 in hybrid mode vs. full autonomous mode.
18. What preventive maintenance is needed for a PG-P01 over its first 2 years?
19. If I expand my PG-C01 battery capacity, what other considerations should I have?
20. What's the complete troubleshooting workflow for a battery not charging issue?

---

## 🎓 Conseils Pédagogiques

### Pour les Élèves "Fainéants"
- Commencer avec questions simples (Niveau 1)
- Interface chatbot simple avec réponses pré-formatées
- Focus sur l'utilisation, pas l'implémentation

### Pour les Élèves "Moteurs"
- Questions complexes multi-hop (Niveau 3-4)
- Accès au code source du RAG/GraphRAG
- Missions : optimiser les requêtes, améliorer le graphe
- Challenge : ajouter de nouvelles relations au knowledge graph

### Activités de Groupe Suggérées
1. **Compétition de Prompt** : Qui peut faire le meilleur prompt pour une question complexe ?
2. **Chasse aux Hallucinations** : Trouver les réponses incorrectes du chatbot
3. **Design de Graphe** : Dessiner le knowledge graph sur tableau blanc
4. **Cas Pratique** : Client appelle avec problème E04, utiliser RAG vs GraphRAG pour le guider

---

## ⚠️ Notes Importantes

### Différences avec ECOLOGENE réel :
- **Nom société :** GreenPower Solutions (pas Ecologene)
- **Acronymes produits :** PG-XX (pas ECOLOGENE® XX)
- **URLs :** greenpower.com (pas ecologene.fr)
- **Documents :** Manual_PG-XX (pas identiques aux vrais)
- **CEO fictif :** Vincent Theroux (inspiré de Vincent Theven)

### Cohérence du Dataset :
✅ Toutes les références croisées sont cohérentes  
✅ Les chiffres (prix, specs, CO2) sont réalistes mais fictifs  
✅ Les dates d'événements sont cohérentes (2024-2025)  
✅ Les localisations géographiques sont basées sur les vraies (Perpignan, Bordeaux, etc.)

### Prochaines Étapes (si besoin) :
1. Créer dataset pour "EKALAND" (équivalent Ekoland)
2. Ajouter plus d'événements (50+ pour tester scalabilité GraphRAG)
3. Générer des transcripts de calls clients (audio → text)
4. Créer des vidéos/images de démo (pour multimodal RAG)

---

## 📧 Contact

**Pour questions sur le dataset :**  
Adrian (@Mensaflow) - adrian@mensaflow.com

**Dataset créé par :** Claude (Anthropic)  
**Date :** 6 janvier 2026  
**Version :** 1.0

---

**Bon courage pour la formation AI4Industry ! 🚀**
