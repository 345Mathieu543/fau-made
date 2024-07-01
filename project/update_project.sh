#!/bin/bash

# Set working directory
cd $(dirname "$0")

# Execute pipelines
./pipeline.sh

# Update plots
pip install nbconvert[webpdf] > /dev/null
jupyter nbconvert --execute --to notebook --inplace ./data-exploration.ipynb  > /dev/null 2>&1 
echo "[INFO] Plots updated"

# Upddate analysis
echo "[INFO] Analysis updated:"
python3 ./analysis.py

# Update reports
pandoc data-report.md -o data-report.pdf -V papersize:a4 -V geometry:margin=2cm
pandoc analysis-report.md -o analysis-report.pdf
echo "[INFO] Reports updated"
