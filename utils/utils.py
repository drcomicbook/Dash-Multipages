import os
from pathlib import Path
from importlib import import_module

import dash

ROOT_DIR = Path(__file__).parent.parent
DEMO_APPS_DIR_NAME = "demos"

DEMOS_APPS_DIR = os.path.join(ROOT_DIR, DEMO_APPS_DIR_NAME)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")


def filter_registry():
    """
    Returns a filtered dash.page_registry dict based on a list of example app names
    """
    # We use the module param to filter the dash_page_registry
    # Note that the module name includes the pages folder name eg: "pages.bar-charts"
    filtered_registry = []
    for page in dash.page_registry.values():
        filtered_registry.append(page)
    return filtered_registry


def project_names():
    projects = []
    for project in os.listdir(DEMOS_APPS_DIR):
        if not project.startswith("_") and project.endswith(".py"):
            project = project.replace(".py", "")
            if project in projects:
                raise Exception(
                    f"Project names must be unique. '{project}.py` already exists"
                )
            projects.append(project)
    return projects


project_names = project_names()

project_moduls = {p: import_module(f"{DEMO_APPS_DIR_NAME}.{p}") for p in project_names}
project_apps = {p: m.app for p, m in project_moduls.items()}
