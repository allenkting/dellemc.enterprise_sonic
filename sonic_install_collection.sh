#!/bin/bash

# Define variables
PROJECT_DIR="/home/$USERNAME/ansible-venv/sonic-ans/ansible-github/dellemc.enterprise_sonic"
REQUIREMENTS_FILE="$PROJECT_DIR/../requirements.yml"

# Populate requirements.yml
cat <<EOL > $REQUIREMENTS_FILE
# requirements.yml
collections:
  - source: ./dellemc.enterprise_sonic
    type: dir
EOL

# Install the Ansible collection
cd $PROJECT_DIR
cd ..
ansible-galaxy collection install -r ./requirements.yml --force
cd dellemc.enterprise_sonic