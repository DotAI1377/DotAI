#!/bin/bash

# Script to deploy the AIris AI application

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
APP_NAME="AIrisAI"
BACKEND_DIR="backend"
FRONTEND_DIR="frontend"
SERVER="your-server-address"
DEPLOY_DIR="/var/www/$APP_NAME"

# Functions
function deploy_backend() {
    echo "Deploying backend..."
    ssh $SERVER "mkdir -p $DEPLOY_DIR/backend"
    scp -r $BACKEND_DIR/* $SERVER:$DEPLOY_DIR/backend
    ssh $SERVER "cd $DEPLOY_DIR/backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
}

function deploy_frontend() {
    echo "Deploying frontend..."
    ssh $SERVER "mkdir -p $DEPLOY_DIR/frontend"
    cd $FRONTEND_DIR
    npm run build
    scp -r build/* $SERVER:$DEPLOY_DIR/frontend
    cd ..
}

function restart_services() {
    echo "Restarting services..."
    ssh $SERVER "sudo systemctl restart $APP_NAME-backend"
    ssh $SERVER "sudo systemctl restart $APP_NAME-frontend"
}

# Main Deployment Process
echo "Starting deployment for $APP_NAME"
deploy_backend
deploy_frontend
restart_services
echo "Deployment completed successfully."
