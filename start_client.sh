#!/bin/bash

# Ativa o virtualenv
source .venv/bin/activate

# Roda a aplicação
export FLASK_APP=client/client.py
flask run
