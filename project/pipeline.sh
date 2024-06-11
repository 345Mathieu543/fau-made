#!/bin/bash
cd $(dirname "$0")
python3 ./pipeline1.py
rm ../data/data.sqlite 2> /dev/null
jv ./pipeline2.jv
python3 ./pipeline3.py