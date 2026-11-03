"""
Vercel Serverless Function Entry Point
======================================
This file serves as the entry point for deploying the FastAPI backend
on Vercel's serverless platform.

It uses Mangum to adapt the FastAPI application into an AWS Lambda handler,
which is the underlying runtime that Vercel uses for Python functions.

Key Notes:
- lifespan="off" is set because Vercel serverless functions don't support
  ASGI lifespan events (startup/shutdown hooks).
- The parent directory is added to sys.path so that imports from the
  backend root (like `app`, `config`, `services`, etc.) work correctly.
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from mangum import Mangum
from app import app

handler = Mangum(app, lifespan="off")