#!/bin/bash

# Script to set up the environment for AIris AI application

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
PYTHON_VERSION="python3"
VENV_DIR="venv"
FRONTEND_DIR="frontend"

# Functions
function setup_backend_env() {
    echo "Setting up backend environment..."
    if [ ! -d "$VENV_DIR" ]; then
        $PYTHON_VERSION -m venv $VENV_DIR
    fi
    source $VENV_DIR/bin/activate
    pip install --upgrade pip
    pip install -r backend/requirements.txt
    deactivate
}

function setup_frontend_env() {
    echo "Setting up frontend environment..."
    cd $FRONTEND_DIR
    if [ ! -d "node_modules" ]; then
        npm install
    fi
    cd ..
}

# Main Setup Process
echo "Starting environment setup..."
setup_backend_env
setup_frontend_env
echo "Environment setup completed successfully."
