FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	TASKS_FILE_PATH=/data/tasks.json

WORKDIR /app

RUN apt-get update \
	&& apt-get install -y --no-install-recommends ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Code applicatif
COPY task_manager ./task_manager

# ✅ Tests (CRITIQUE)
COPY tests ./tests

COPY README.md .

RUN useradd -m appuser \
	&& mkdir -p /data /app/logs \
	&& chown -R appuser:appuser /app /data

USER appuser

ENTRYPOINT ["python", "-m", "task_manager.cli"]