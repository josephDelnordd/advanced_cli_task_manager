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
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── README.md
├── requirements.txt
├── tasks.json                 # Fichier de persistance des tâches
├── logs/
│   └── task_manager.log       # Logs applicatifs (local)
├── task_manager/
│   ├── cli.py                 # Point d’entrée CLI
│   ├── core.py                # Logique métier
│   ├── config.py              # Gestion de la configuration
│   └── logger.py              # Configuration du logging
└── tests/
    └── test_core.py           # Tests unitaires
```

---

## ⚙️ Prérequis

### Exécution locale

- Python ≥ 3.10
- pip
- (Recommandé) Environnement virtuel Python

### Exécution Docker

- Docker ≥ 20.x
- Docker Compose v2

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

## 🐳 Utilisation avec Docker

Le projet est entièrement **containerisé**.

### 🔨 Build de l’image

```bash
make docker-build
```

### 📋 Lister les tâches

```bash
make docker-list
```

### ➕ Ajouter une tâche

```bash
make docker-add TASK="Buy milk" PRIORITY=high
```

### ❌ Supprimer une tâche

```bash
make docker-delete ID=1
```

✅ Les données sont persistées via `tasks.json`.
✅ Les logs sont compatibles stdout Docker (cloud‑native).

---

## 🧪 Tests automatisés

### Exécution locale

```bash
make test
```

### Exécution dans Docker

```bash
make docker-test
```

✅ Les tests sont :

- isolés
- reproductibles
- indépendants des données locales

---

## 🧹 Nettoyage

### Nettoyage local

```bash
make clean
```

Supprime :

- tous les `__pycache__` (récursivement)
- fichiers .pyc
- cache pytest
- logs locaux

### Nettoyage complet (local + Docker)

```bash
make clean-all
```

Supprime :

- containers Docker
- volumes
- image Docker du projet

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

✅ En environnement Docker / CI, les logs sont envoyés sur stdout
✅ En local, ils peuvent être écrits dans logs/task_manager.log

---

## 🏁 Conclusion

Advanced CLI Task Manager est un projet pédagogique et technique démontrant :

- le développement d’un CLI Python structuré
- l’utilisation de Docker de manière propre et sécurisée
- l’orchestration via Makefile
- une approche reproductible et CI‑ready

C’est une base saine pour :

- apprendre les bonnes pratiques CLI
- servir de socle à un projet DevOps
- être étendu (CI/CD, packaging, Kubernetes, etc.)