# BFS and DFS Algorithm Comparison: Python vs Go

This project implements Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms in both Python and Go to compare their performance.

## Project Structure

- `graph.py` - Graph structure implementation in Python
- `graph.go` - Graph structure implementation in Go
- `python_bfs_dfs.py` - BFS and DFS implementations in Python
- `go_bfs_dfs.go` - BFS and DFS implementations in Go
- `main.go` - Entry point for Go implementation
- `main.py` - Main script to run and compare both implementations

## Requirements

- Python 3.6+
- Go 1.13+

## Running the Comparison

1. Make sure you have both Python and Go installed on your system.
2. Navigate to the project directory.
3. Run the comparison script:

```bash
python main.py [graph_size]
```

Where `graph_size` is an optional parameter to specify the number of vertices in the test graph (default is 1000).

## What's Being Compared

The project compares the performance of:

1. BFS implementation in Python vs Go
2. Recursive DFS implementation in Python vs Go
3. Iterative DFS implementation in Python vs Go

The comparison includes:
- Execution time for each algorithm
- Total execution time for each language
- Speedup ratio between Go and Python

## Graph Structure

The test graph is created with the following properties:

- A basic linear path connecting all vertices
- Cross connections for every 10th node to create shortcuts
- Backward edges for every 20th node to create cycles

This structure provides a good mix of short and long paths to test both BFS and DFS algorithms effectively.