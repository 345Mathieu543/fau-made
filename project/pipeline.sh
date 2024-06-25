#!/bin/bash

# Set Working Directory
cd $(dirname "$0")

# Execute Pipelines
python3 ./pipeline1.py
rm ../data/data.sqlite 2> /dev/null
jv ./pipeline2.jv
python3 ./pipeline3.py

# Update plots
pip install nbconvert[webpdf]
jupyter nbconvert --execute --to notebook --inplace ./data-exploration.ipynb

# Update reports
pandoc data-report.md     -o data-report.pdf     -V papersize:a4 -V geometry:margin=2cm
pandoc analysis-report.md -o analysis-report.pdf -V papersize:a4 -V geometry:margin=2cm
