// This file defines a graph structure for BFS and DFS algorithms

package main

import "fmt"

// Graph represents a directed graph using adjacency list
type Graph struct {
	NumVertices int
	AdjList     [][]int
}

// NewGraph creates a new graph with the specified number of vertices
func NewGraph(numVertices int) *Graph {
	adjList := make([][]int, numVertices)
	for i := range adjList {
		adjList[i] = make([]int, 0)
	}
	return &Graph{
		NumVertices: numVertices,
		AdjList:     adjList,
	}
}

// AddEdge adds an edge from src to dest
func (g *Graph) AddEdge(src, dest int) {
	g.AdjList[src] = append(g.AdjList[src], dest)
}

// GetAdjacencyList returns the adjacency list
func (g *Graph) GetAdjacencyList() [][]int {
	return g.AdjList
}

// GetNumVertices returns the number of vertices
func (g *Graph) GetNumVertices() int {
	return g.NumVertices
}

// CreateTestGraph creates a test graph with a specified number of vertices
// The graph is structured to have a mix of short and long paths
// to test both BFS and DFS algorithms effectively
func CreateTestGraph(size int) *Graph {
	g := NewGraph(size)

	// Create a basic structure with some branching
	for i := 0; i < size-1; i++ {
		// Connect to next node (creates a long path)
		g.AddEdge(i, i+1)

		// Add some cross connections for every 10th node
		if i%10 == 0 {
			// Connect to nodes further ahead to create shortcuts
			for j := 1; j <= 5; j++ { // Connect to 5 nodes ahead with varying distances
				if i+j*10 < size {
					g.AddEdge(i, i+j*10)
				}
			}
		}

		// Add some backward edges for every 20th node
		if i%20 == 0 && i > 0 {
			// Connect back to create cycles
			g.AddEdge(i, i/2)
		}
	}

	return g
}

// CreateBinaryTree creates a binary tree with the specified number of nodes
// Each node (except leaf nodes) has exactly two children
// The rightmost leaf node is the target for search algorithms
func CreateBinaryTree(size int) *Graph {
	g := NewGraph(size)

	// For a binary tree, each node i has children 2i+1 and 2i+2
	// (except for nodes that would exceed the size)
	for i := 0; i < size; i++ {
		// Add left child if within bounds
		leftChild := 2*i + 1
		if leftChild < size {
			g.AddEdge(i, leftChild)
		}

		// Add right child if within bounds
		rightChild := 2*i + 2
		if rightChild < size {
			g.AddEdge(i, rightChild)
		}
	}

	return g
}

// ExampleUsage demonstrates how to use the graph
func ExampleUsage() {
	// Create a small graph for demonstration
	g := CreateTestGraph(20)

	fmt.Println("Adjacency List:")
	adjList := g.GetAdjacencyList()
	for i, neighbors := range adjList {
		fmt.Printf("Vertex %d: %v\n", i, neighbors)
	}
}