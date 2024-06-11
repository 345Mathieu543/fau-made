#!/bin/bash
cd $(dirname "$0")
python3 ./pipeline1.py
rm ../data/data.sqlite
jv ./pipeline2.jv
python3 ./pipeline3.py