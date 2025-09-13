# python_bfs_dfs.py
# Implementation of BFS and DFS algorithms in Python

from collections import deque
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from graph import Graph, create_test_graph

def bfs(graph, start_vertex):
    """
    Breadth-First Search algorithm implementation.
    
    Args:
        graph: Graph object with adjacency list representation
        start_vertex: Starting vertex for the search
        
    Returns:
        List of vertices in the order they were visited
    """
    num_vertices = graph.get_num_vertices()
    visited = [False] * num_vertices
    queue = deque([start_vertex])
    visited[start_vertex] = True
    visited_order = [start_vertex]
    
    while queue:
        vertex = queue.popleft()
        
        # Visit all adjacent vertices
        for adjacent in graph.adj_list[vertex]:
            if not visited[adjacent]:
                visited[adjacent] = True
                visited_order.append(adjacent)
                queue.append(adjacent)
    
    return visited_order

def dfs_recursive(graph, vertex, visited, visited_order):
    """
    Helper function for recursive DFS implementation.
    
    Args:
        graph: Graph object with adjacency list representation
        vertex: Current vertex being visited
        visited: List tracking visited vertices
        visited_order: List to store the order of visited vertices
    """
    visited[vertex] = True
    visited_order.append(vertex)
    
    for adjacent in graph.adj_list[vertex]:
        if not visited[adjacent]:
            dfs_recursive(graph, adjacent, visited, visited_order)

def dfs(graph, start_vertex):
    """
    Depth-First Search algorithm implementation using recursion.
    
    Args:
        graph: Graph object with adjacency list representation
        start_vertex: Starting vertex for the search
        
    Returns:
        List of vertices in the order they were visited
    """
    num_vertices = graph.get_num_vertices()
    visited = [False] * num_vertices
    visited_order = []
    
    dfs_recursive(graph, start_vertex, visited, visited_order)
    
    return visited_order

def dfs_iterative(graph, start_vertex):
    """
    Depth-First Search algorithm implementation using iteration (stack).
    
    Args:
        graph: Graph object with adjacency list representation
        start_vertex: Starting vertex for the search
        
    Returns:
        List of vertices in the order they were visited
    """
    num_vertices = graph.get_num_vertices()
    visited = [False] * num_vertices
    stack = [start_vertex]
    visited_order = []
    
    while stack:
        vertex = stack.pop()
        
        if not visited[vertex]:
            visited[vertex] = True
            visited_order.append(vertex)
            
            # Add adjacent vertices in reverse order to maintain DFS property
            for adjacent in reversed(graph.adj_list[vertex]):
                if not visited[adjacent]:
                    stack.append(adjacent)
    
    return visited_order

def measure_performance(graph, start_vertex=0):
    """
    Measure the performance of BFS and DFS algorithms.
    
    Args:
        graph: Graph object with adjacency list representation
        start_vertex: Starting vertex for the search
        
    Returns:
        Dictionary with execution times for each algorithm
    """
    results = {}
    
    # Measure BFS performance
    start_time = time.time()
    bfs_result = bfs(graph, start_vertex)
    end_time = time.time()
    results['bfs'] = {
        'time': end_time - start_time,
        'visited_count': len(bfs_result)
    }
    
    # Skip recursive DFS due to recursion depth limitations with large graphs
    # Instead, we'll use the iterative implementation for both DFS measurements
    results['dfs_recursive'] = {
        'time': 0,
        'visited_count': 0,
        'skipped': True
    }
    
    # Measure iterative DFS performance
    start_time = time.time()
    dfs_iter_result = dfs_iterative(graph, start_vertex)
    end_time = time.time()
    results['dfs_iterative'] = {
        'time': end_time - start_time,
        'visited_count': len(dfs_iter_result)
    }
    
    return results

def run_concurrent_searches(graph, algorithm, start_vertices, num_threads):
    """
    Run searches concurrently using multiple threads.
    
    Args:
        graph: Graph object with adjacency list representation
        algorithm: The search algorithm function to use (bfs or dfs_iterative)
        start_vertices: List of starting vertices for the searches
        num_threads: Number of concurrent threads to use
        
    Returns:
        Dictionary with execution time and total visited count
    """
    results = []
    
    def worker(vertex):
        start_time = time.time()
        visited = algorithm(graph, vertex)
        end_time = time.time()
        return {
            'time': end_time - start_time,
            'visited_count': len(visited),
            'vertex': vertex
        }
    
    # Use ThreadPoolExecutor to run searches concurrently
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(worker, start_vertices))
    
    # Calculate total time (max of all thread times) and total visited count
    total_time = max(result['time'] for result in results)
    total_visited = sum(result['visited_count'] for result in results)
    
    return {
        'time': total_time,  # Time is the max time of all threads (real concurrent time)
        'visited_count': total_visited,
        'thread_results': results
    }

def measure_concurrent_performance(graph, concurrency=1, start_vertex=0):
    """
    Measure the performance of BFS and DFS algorithms with concurrency.
    
    Args:
        graph: Graph object with adjacency list representation
        concurrency: Number of concurrent searches to run
        start_vertex: Base starting vertex for the search
        
    Returns:
        Dictionary with execution times for each algorithm
    """
    results = {}
    
    # Generate different starting vertices for concurrent searches
    # We'll use different vertices to ensure threads are doing different work
    start_vertices = []
    for i in range(concurrency):
        # Distribute starting vertices across the graph
        vertex = (start_vertex + i * (graph.get_num_vertices() // (concurrency + 1))) % graph.get_num_vertices()
        start_vertices.append(vertex)
    
    # Measure concurrent BFS performance
    results['bfs'] = run_concurrent_searches(graph, bfs, start_vertices, concurrency)
    
    # Skip recursive DFS due to recursion depth limitations with large graphs
    results['dfs_recursive'] = {
        'time': 0,
        'visited_count': 0,
        'skipped': True
    }
    
    # Measure concurrent iterative DFS performance
    results['dfs_iterative'] = run_concurrent_searches(graph, dfs_iterative, start_vertices, concurrency)
    
    return results

def run_python_benchmark(graph_size=1000, start_vertex=0, concurrency=1, use_binary_tree=False):
    """
    Run benchmark for Python BFS and DFS implementations.
    
    Args:
        graph_size: Size of the graph to create
        start_vertex: Starting vertex for the search
        concurrency: Number of concurrent searches to run
        use_binary_tree: Whether to use a binary tree instead of the default test graph
        
    Returns:
        Dictionary with benchmark results
    """
    print(f"\nRunning Python BFS/DFS benchmark with graph size {graph_size} and concurrency {concurrency}...")
    
    # Import the graph creation functions
    from graph import create_test_graph, create_binary_tree
    
    # Create the appropriate graph
    if use_binary_tree:
        graph = create_binary_tree(graph_size)
        print(f"Created binary tree with {graph_size} nodes")
    else:
        graph = create_test_graph(graph_size)
        print(f"Created test graph with {graph_size} vertices")
    
    if concurrency <= 1:
        # Run single-threaded benchmark
        results = measure_performance(graph, start_vertex)
    else:
        # Run concurrent benchmark
        results = measure_concurrent_performance(graph, concurrency, start_vertex)
    
    print("\nPython Results:")
    print(f"BFS Time: {results['bfs']['time']:.10f} seconds, Visited: {results['bfs']['visited_count']} nodes")
    print(f"DFS (Recursive): Skipped due to Python recursion depth limitations with large graphs")
    print(f"DFS (Iterative) Time: {results['dfs_iterative']['time']:.10f} seconds, Visited: {results['dfs_iterative']['visited_count']} nodes")
    
    return results

if __name__ == "__main__":
    # Run a simple test
    run_python_benchmark(1000)