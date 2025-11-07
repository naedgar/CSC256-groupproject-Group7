#!/usr/bin/env python3
"""
Quick script to test writing to /tmp/tasks.db using SQLAlchemy.
"""
import os
import traceback
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

DB_PATH = "/tmp/tasks.db"
URI = f"sqlite:///{DB_PATH}"

print(f"Testing write to {DB_PATH} using URI {URI}")

try:
    engine = create_engine(URI)
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS demo (id INTEGER PRIMARY KEY, name TEXT)"))
        conn.execute(text("INSERT INTO demo (name) VALUES (:name)"), {"name": "test-entry"})
        count = conn.execute(text("SELECT COUNT(*) FROM demo")).scalar()
    print(f"Write succeeded, demo rows = {count}")
    engine.dispose()
except OperationalError as oe:
    print("OperationalError encountered:\n", oe)
    traceback.print_exc()
    raise
except Exception as e:
    print("Unexpected exception:\n", e)
    traceback.print_exc()
    raise
