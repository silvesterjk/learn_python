// Implementation of BFS and DFS algorithms in Go

package main

import (
	"fmt"
	"sync"
	"time"
)

// BFS and DFS algorithm implementations
// Graph struct and related functions are defined in graph.go

// BFS performs breadth-first search on the graph starting from the given vertex
func BFS(graph *Graph, startVertex int) []int {
	numVertices := graph.NumVertices
	visited := make([]bool, numVertices)
	queue := []int{startVertex}
	visitedOrder := []int{startVertex}
	visited[startVertex] = true

	for len(queue) > 0 {
		// Dequeue a vertex from queue
		vertex := queue[0]
		queue = queue[1:]

		// Visit all adjacent vertices
		for _, adjacent := range graph.AdjList[vertex] {
			if !visited[adjacent] {
				visited[adjacent] = true
				visitedOrder = append(visitedOrder, adjacent)
				queue = append(queue, adjacent)
			}
		}
	}

	return visitedOrder
}

// dfsRecursive is a helper function for recursive DFS implementation
func dfsRecursive(graph *Graph, vertex int, visited []bool, visitedOrder *[]int) {
	visited[vertex] = true
	*visitedOrder = append(*visitedOrder, vertex)

	for _, adjacent := range graph.AdjList[vertex] {
		if !visited[adjacent] {
			dfsRecursive(graph, adjacent, visited, visitedOrder)
		}
	}
}

// DFS performs depth-first search on the graph starting from the given vertex
func DFS(graph *Graph, startVertex int) []int {
	numVertices := graph.NumVertices
	visited := make([]bool, numVertices)
	visitedOrder := []int{}

	dfsRecursive(graph, startVertex, visited, &visitedOrder)

	return visitedOrder
}

// DFSIterative performs depth-first search on the graph starting from the given vertex using an iterative approach
func DFSIterative(graph *Graph, startVertex int) []int {
	numVertices := graph.NumVertices
	visited := make([]bool, numVertices)
	stack := []int{startVertex}
	visitedOrder := []int{}

	for len(stack) > 0 {
		// Pop a vertex from stack
		vertex := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if !visited[vertex] {
			visited[vertex] = true
			visitedOrder = append(visitedOrder, vertex)

			// Add adjacent vertices in reverse order to maintain DFS property
			for i := len(graph.AdjList[vertex]) - 1; i >= 0; i-- {
				adjacent := graph.AdjList[vertex][i]
				if !visited[adjacent] {
					stack = append(stack, adjacent)
				}
			}
		}
	}

	return visitedOrder
}

// Result represents the performance measurement result
type Result struct {
	Time         float64
	VisitedCount int
}

// ThreadResult represents the result of a single thread/goroutine
type ThreadResult struct {
	Time         float64
	VisitedCount int
	Vertex       int
}

// RunConcurrentSearches runs multiple searches concurrently using goroutines
func RunConcurrentSearches(graph *Graph, algorithm func(*Graph, int) []int, startVertices []int, numThreads int) Result {
	results := make([]ThreadResult, len(startVertices))
	var wg sync.WaitGroup

	// Create a worker function that will be executed by each goroutine
	worker := func(index int, vertex int) {
		defer wg.Done()
		startTime := time.Now()
		visited := algorithm(graph, vertex)
		elapsed := time.Since(startTime).Seconds()
		results[index] = ThreadResult{
			Time:         elapsed,
			VisitedCount: len(visited),
			Vertex:       vertex,
		}
	}

	// Launch goroutines
	for i, vertex := range startVertices {
		wg.Add(1)
		go worker(i, vertex)
	}

	// Wait for all goroutines to complete
	wg.Wait()

	// Calculate total time (max of all goroutine times) and total visited count
	var totalTime float64
	totalVisited := 0

	for _, result := range results {
		if result.Time > totalTime {
			totalTime = result.Time
		}
		totalVisited += result.VisitedCount
	}

	return Result{
		Time:         totalTime, // Time is the max time of all goroutines (real concurrent time)
		VisitedCount: totalVisited,
	}
}

// MeasureConcurrentPerformance measures the performance of concurrent BFS and DFS
func MeasureConcurrentPerformance(graph *Graph, concurrency int, startVertex int) map[string]Result {
	results := make(map[string]Result)

	// Generate different starting vertices for concurrent searches
	// We'll use different vertices to ensure goroutines are doing different work
	startVertices := make([]int, concurrency)
	for i := 0; i < concurrency; i++ {
		// Distribute starting vertices across the graph
		vertex := (startVertex + i*(graph.NumVertices/(concurrency+1))) % graph.NumVertices
		startVertices[i] = vertex
	}

	// Measure concurrent BFS performance
	results["bfs"] = RunConcurrentSearches(graph, BFS, startVertices, concurrency)

	// Measure concurrent recursive DFS performance
	results["dfs_recursive"] = RunConcurrentSearches(graph, DFS, startVertices, concurrency)

	// Measure concurrent iterative DFS performance
	results["dfs_iterative"] = RunConcurrentSearches(graph, DFSIterative, startVertices, concurrency)

	return results
}

// MeasurePerformance measures the performance of BFS and DFS algorithms
func MeasurePerformance(graph *Graph, startVertex int) map[string]Result {
	results := make(map[string]Result)

	// Measure BFS performance
	start := time.Now()
	visitedBFS := BFS(graph, startVertex)
	bfsTime := time.Since(start).Seconds()
	fmt.Printf("BFS Time: %.6f seconds, Visited: %d nodes\n", bfsTime, len(visitedBFS))
	results["bfs"] = Result{Time: bfsTime, VisitedCount: len(visitedBFS)}

	// Measure recursive DFS performance
	start = time.Now()
	visitedDFS := DFS(graph, startVertex)
	dfsTime := time.Since(start).Seconds()
	fmt.Printf("DFS (Recursive) Time: %.6f seconds, Visited: %d nodes\n", dfsTime, len(visitedDFS))
	results["dfs_recursive"] = Result{Time: dfsTime, VisitedCount: len(visitedDFS)}

	// Measure iterative DFS performance
	start = time.Now()
	visitedDFSIter := DFSIterative(graph, startVertex)
	dfsIterTime := time.Since(start).Seconds()
	fmt.Printf("DFS (Iterative) Time: %.6f seconds, Visited: %d nodes\n", dfsIterTime, len(visitedDFSIter))
	results["dfs_iterative"] = Result{Time: dfsIterTime, VisitedCount: len(visitedDFSIter)}

	return results
}

// RunGoBenchmark runs benchmark for Go BFS and DFS implementations
func RunGoBenchmark(graphSize int, concurrency int, useBinaryTree bool) map[string]Result {
	fmt.Printf("\nRunning Go BFS/DFS benchmark with graph size %d and concurrency %d...\n", graphSize, concurrency)
	
	// Create the appropriate graph based on the useBinaryTree flag
	var graph *Graph
	if useBinaryTree {
		graph = CreateBinaryTree(graphSize)
		fmt.Printf("Using binary tree with %d nodes\n", graphSize)
	} else {
		graph = CreateTestGraph(graphSize)
		fmt.Printf("Using test graph with %d vertices\n", graphSize)
	}
	
	var results map[string]Result
	// Use 0 as the start vertex
	const startVertex = 0
	if concurrency <= 1 {
		// Run single-threaded benchmark
		results = MeasurePerformance(graph, startVertex)
	} else {
		// Run concurrent benchmark
		results = MeasureConcurrentPerformance(graph, concurrency, startVertex)
	}

	fmt.Println("\nGo Results:")
	fmt.Printf("BFS Time: %.10f seconds, Visited: %d nodes\n", 
		results["bfs"].Time, results["bfs"].VisitedCount)
	fmt.Printf("DFS (Recursive) Time: %.10f seconds, Visited: %d nodes\n", 
		results["dfs_recursive"].Time, results["dfs_recursive"].VisitedCount)
	fmt.Printf("DFS (Iterative) Time: %.10f seconds, Visited: %d nodes\n", 
		results["dfs_iterative"].Time, results["dfs_iterative"].VisitedCount)

	return results
}