# Advanced CLI Task Manager

## Usage
```bash
python -m task_manager.cli add "Buy milk" --priority high
python -m task_manager.cli list
python -m task_manager.cli delete 1
```

## Environment Variable

```bash
export TASKS_FILE_PATH=tasks.json
```

## Tests

```bash
python -m unittest discover tests
```

## ✅ Exemples d’exécution

```bash
python -m task_manager.cli add "Deploy app" --priority high
python -m task_manager.cli list
python -m task_manager.cli delete 1
```

✔ JSON ✅
✔ subcommands ✅
✔ env var ✅
✔ logging ✅
✔ tests ✅
