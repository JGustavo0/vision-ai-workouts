#!/bin/bash

ENV_NAME="visionfit"
ENV_FILE="environment.yml"

# Check if the Conda environment exists
if conda info --envs | grep -q "$ENV_NAME"; then
    echo "Conda environment '$ENV_NAME' already exists."
else
    # Create the Conda environment from the file
    echo "Creating Conda environment '$ENV_NAME'..."
    conda env create -f "$ENV_FILE"
    echo "Environment '$ENV_NAME' created successfully."
fi

# Activate the environment
echo "Activating the Conda environment '$ENV_NAME'..."
source activate "$ENV_NAME"
