#!/usr/bin/python3
"""This package contains all the classes used in the application

Modules:
    base_model

Sub-packages:
    engine

Attributes:
    storage (FileStorage): A unique FileStorage instance for our application.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
