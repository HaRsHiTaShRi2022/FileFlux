#!/usr/bin/env bash\

echo "Installing LibreOffice..."
apt-get update && apt-get install -y libreoffice libreoffice-common libreoffice-core

echo "Starting Gunicorn..."
gunicorn Main:app
