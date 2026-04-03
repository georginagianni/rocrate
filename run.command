#!/bin/bash

cd "$(dirname "$0")"

echo "Activating environment..."
source .venv/bin/activate

echo "Running pipeline..."
python3 src/main.py

if [ $? -eq 0 ]; then
  echo "Opening Jupyter Lab..."
  jupyter lab notebooks/analysis.ipynb
else
  echo "Pipeline failed. Jupyter will not open."
fi