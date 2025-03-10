#!/usr/bin/env bash

echo "Installing LibreOffice..."
apt-get update && apt-get install -y libreoffice

echo "Starting Gunicorn..."
gunicorn Main:app
