#!/usr/bin/env bash
# Exit on error
set -e

echo "Installing dependencies..."
apt-get update
apt-get install -y libreoffice

echo "LibreOffice installation completed"
echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Build script completed successfully"
