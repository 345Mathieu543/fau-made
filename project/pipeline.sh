#!/bin/bash
cd $(dirname "$0")
python3 ./getPedData.py
jv -d ./pipeline.jv