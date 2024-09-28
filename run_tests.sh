#!/bin/bash -e

if [ ! -d .venv ]; then
    virtualenv .venv
fi
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest

pytest

