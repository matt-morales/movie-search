#!/bin/bash

echo "Installing challenge package for live development.."
pip install -e .

echo "Starting server.."
flask run --host=0.0.0.0 --port=80
