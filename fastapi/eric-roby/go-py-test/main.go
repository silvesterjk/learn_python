// Main entry point for Go BFS and DFS implementation

package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	// Default values
	graphSize := 50000
	concurrency := 1
	useBinaryTree := false

	// Parse command line arguments if provided
	if len(os.Args) > 1 {
		size, err := strconv.Atoi(os.Args[1])
		if err == nil && size > 0 {
			graphSize = size
		} else {
			fmt.Printf("Invalid graph size: %s. Using default size %d.\n", os.Args[1], graphSize)
		}
	}

	// Parse concurrency if provided as second argument
	if len(os.Args) > 2 {
		conc, err := strconv.Atoi(os.Args[2])
		if err == nil && conc > 0 {
			concurrency = conc
		} else {
			fmt.Printf("Invalid concurrency: %s. Using default concurrency %d.\n", os.Args[2], concurrency)
		}
	}

	// Check for binary tree flag
	if len(os.Args) > 3 && os.Args[3] == "binary" {
		useBinaryTree = true
		fmt.Println("Using binary tree structure for testing")
	}

	// Run the benchmark
	results := RunGoBenchmark(graphSize, concurrency, useBinaryTree)
	
	// Print results
	fmt.Println("\nGo Benchmark Results:")
	fmt.Printf("BFS time: %.10fs\n", results["bfs"].Time)
	fmt.Printf("Recursive DFS time: %.10fs\n", results["dfs_recursive"].Time)
	fmt.Printf("Iterative DFS time: %.10fs\n", results["dfs_iterative"].Time)
	
	// Return the results to be used by the Python script
	fmt.Printf("\n===RESULTS_START===\n")
	fmt.Printf("bfs:%.10f\n", results["bfs"].Time)
	fmt.Printf("dfs_recursive:%.10f\n", results["dfs_recursive"].Time)
	fmt.Printf("dfs_iterative:%.10f\n", results["dfs_iterative"].Time)
	fmt.Printf("===RESULTS_END===\n")
}