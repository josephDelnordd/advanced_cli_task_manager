# 🧰 Advanced CLI Task Manager

**Advanced CLI Task Manager** est un outil **en ligne de commande (CLI)** développé en Python permettant de **gérer des tâches** (ajout, listing, suppression) avec des **fonctionnalités avancées** orientées bonnes pratiques DevOps.

Le projet met en œuvre :

- ✅ des **sous‑commandes CLI** avec `argparse`
- ✅ une **persistance en JSON**
- ✅ une **configuration par variable d’environnement**
- ✅ un **système de logging**
- ✅ des **tests unitaires automatisés**

---

## 🧱 Architecture du projet

```text
.
├── README.md
├── requirements.txt
├── tasks.json                 # Fichier de persistance des tâches
├── logs/
│   └── task_manager.log       # Logs applicatifs
├── task_manager/
│   ├── cli.py                 # Point d’entrée CLI
│   ├── core.py                # Logique métier
│   ├── config.py              # Gestion de la configuration
│   └── logger.py              # Configuration du logging
└── tests/
    └── test_core.py            # Tests unitaires
```

---

## ⚙️ Prérequis
- Python ≥ 3.10
- pip
- (Recommandé) Environnement virtuel Python

---

## 🚀 Installation

```bash
python -m venv .venv
source .venv/bin/activate      # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Configuration

### Variable d’environnement

Le chemin du fichier JSON contenant les tâches est configurable via la variable :

```bash
export TASKS_FILE_PATH=tasks.json
```

✅ Si la variable n’est pas définie, le projet utilise tasks.json par défaut.

Cette approche permet :

- une exécution locale simple
- une intégration facile en CI/CD
- une séparation claire code / configuration (principe 12‑factor app)

---

## ▶️ Utilisation du CLI

Le CLI s’exécute via le module task_manager.cli.

➕ Ajouter une tâche

```bash
python -m task_manager.cli add "Buy milk" --priority high
```

📋 Lister les tâches
```bash
python -m task_manager.cli list
```

❌ Supprimer une tâche
```bash
python -m task_manager.cli delete 1
```

---

## 📝 Format des données (JSON)

Les tâches sont stockées dans le fichier tasks.json :

```json
[
  {
    "id": 1,
    "description": "Buy milk",
    "priority": "high"
  }
]
```

---

## 📜 Logging

Toutes les actions sont enregistrées dans le fichier :

```bash
logs/task_manager.log
```

Exemples d’événements loggés :

- ajout de tâche
- suppression de tâche
- erreurs métier (ID inexistant, fichier manquant, etc.)

✅ Le système de logs est prêt pour un usage réel ou une intégration CI/CD.

---

## 🧪 Tests automatisés

Les tests unitaires couvrent :

- l’ajout de tâches
- la suppression de tâches
- le chargement et la sauvegarde du fichier JSON

▶️ Lancer les tests

```bash
python -m unittest discover tests
```

✅ Les tests sont isolés, reproductibles et indépendants de l’environnement.

---

## 🏁 Conclusion

**Advanced CLI Task Manager** est un projet complet démontrant les bonnes pratiques de développement d’un outil CLI en Python, avec une attention particulière à la configuration, la persistance, le logging et les tests. C’est une base solide pour construire des outils plus complexes ou pour apprendre les concepts clés du développement logiciel moderne.