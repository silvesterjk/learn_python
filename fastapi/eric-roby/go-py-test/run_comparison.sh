#!/bin/bash
# Simple script to run the BFS/DFS comparison

# Default graph size
GRAPH_SIZE=${1:-1000}

echo "Running BFS/DFS comparison with graph size: $GRAPH_SIZE"

# Make the script executable if it's not already
chmod +x main.py

# Run the comparison
python3 main.py $GRAPH_SIZE