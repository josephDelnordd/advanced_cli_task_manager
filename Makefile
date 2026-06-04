PROJECT_NAME=Advanced-CLI-task-manager
IMAGE_NAME=task-manager
PYTHON=python
DOCKER=docker
DOCKER_COMPOSE=docker compose

.PHONY: help install test run run-help \
docker-build docker-run docker-test \
docker-list docker-add docker-delete \
clean clean-all


help:
	@echo "Commandes disponibles :"
	@echo "  make help -------------------------------------------------------- Affiche cette aide"
	@echo "  make install ----------------------------------------------------- Installe les dépendances"
	@echo "  make test -------------------------------------------------------- Exécute les tests"
	@echo "  make run-help ---------------------------------------------------- Affiche l'aide pour l'exécution en local"
	@echo "  make docker-build ------------------------------------------------ Construit l'image Docker"
	@echo "  make docker-list ------------------------------------------------- Liste les tâches dans Docker"
	@echo "  make docker-add TASK=\"Buy milk\" PRIORITY=high -------------------- Ajoute une tâche dans Docker"
	@echo "  make docker-delete ID=3 ------------------------------------------ Supprime une tâche dans Docker"
	@echo "  make docker-test ------------------------------------------------- Exécute les tests dans Docker"
	@echo "  make clean ------------------------------------------------------- Nettoie les fichiers temporaires"
	@echo "  make clean-all --------------------------------------------------- Nettoie tous les fichiers temporaires"

install:
	pip install -r requirements.txt

test:
	$(PYTHON) -m unittest discover tests

run-help:
	$(PYTHON) -m task_manager.cli --help

docker-build:
	$(DOCKER) build -t $(IMAGE_NAME):latest .

docker-list:
	$(DOCKER_COMPOSE) run --rm task-manager list

docker-add:
	@if [ -z "$(TASK)" ]; then \
		echo "❌ TASK manquant. Exemple : make docker-add TASK=\"Buy milk\" PRIORITY=high"; \
		exit 1; \
	fi
	@if [ -z "$(PRIORITY)" ]; then \
		echo "❌ PRIORITY manquante"; \
		exit 1; \
	fi
	$(DOCKER_COMPOSE) run --rm task-manager add "$(TASK)" --priority "$(PRIORITY)"

docker-delete:
	@if [ -z "$(ID)" ]; then \
		echo "❌ ID manquant. Exemple : make docker-delete ID=3"; \
		exit 1; \
	fi
	$(DOCKER_COMPOSE) run --rm task-manager delete "$(ID)"

docker-test:
	$(DOCKER) run --rm \
		--entrypoint python \
		-e TASKS_FILE_PATH=/tmp/test_tasks.json \
		$(IMAGE_NAME):latest \
		-m unittest discover tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache *.log

clean-all: clean
	$(DOCKER_COMPOSE) down --volumes --remove-orphans
	$(DOCKER) image rm $(IMAGE_NAME):latest || true