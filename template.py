import os
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s], (%(message)s)')

project_name = "PCBDEFECTDETECTION"

list_of_files = [
    "github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/constant/config_entity.py",
    f"{project_name}/constant/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "templates/index.html",
    "research/trails.ipynb",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "test.py",
]

basic_notebook_json = {
    "cells": [],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        if filename.endswith(".ipynb"):
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(basic_notebook_json, f, indent=2)
            logging.info(f"Creating blank Jupyter notebook: {filepath}")
        else:
            with open(filepath, "w", encoding="utf-8") as f:
                pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} is already created")
