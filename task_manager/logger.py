import logging
import os
import sys

def setup_logger(log_file="task_manager.log"):
    logger = logging.getLogger("task_manager")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        log_directory = "logs"
        os.makedirs(log_directory, exist_ok=True)

        file_handler = logging.FileHandler(
            os.path.join(log_directory, log_file)
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    except PermissionError:
        # ✅ Fallback propre (Docker / CI / K8s)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger