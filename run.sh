#!/bin/bash

echo "Activating environment..."
source .venv/bin/activate

echo "Running pipeline..."
python3 src/main.py

