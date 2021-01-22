#!/bin/bash

set -e

echo "Check if user is not root..."
if [ "$EUID" -eq 0 ];
then
  echo "Don't run this script as root!"
  echo "Aborting..."
  exit 1
fi

echo "Installing python3-venv..."
sudo apt-get install python3-venv

echo "Building virtualenv..."
python3 -m venv venv
source venv/bin/activate

echo "Python-venv, Installing flask..."
pip install flask

echo "Python-venv, Installing flask..."
pip install requests

echo "Python-venv, Installing Flask-Webhook..."
sudo apt-get install python3-venv

echo "environment bulding done."

echo "Installation done"
echo "Starting flask"
bash start.sh
