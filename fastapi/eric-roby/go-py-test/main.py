# Main script to run and compare BFS and DFS implementations in Python and Go

import os
import sys
import subprocess
import time
import json
from python_bfs_dfs import run_python_benchmark

def run_go_implementation(graph_size=50000, concurrency=1, use_binary_tree=False):
    """
    Compile and run the Go implementation.
    
    Args:
        graph_size: Number of vertices in the test graph
        concurrency: Number of concurrent searches to run
        use_binary_tree: Whether to use a binary tree instead of the default test graph
        
    Returns:
        Dictionary with benchmark results if successful, None otherwise
    """
    print("\nChecking if Go is installed...")
    try:
        # Check if Go is installed
        check_go = subprocess.run(
            ["which", "go"],
            check=True,
            capture_output=True,
            text=True
        )
        
        print("\nCompiling Go implementation...")
        # Compile the Go code
        compile_process = subprocess.run(
            ["go", "build", "-o", "bfs_dfs_go", "main.go", "graph.go", "go_bfs_dfs.go"],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Run the compiled Go program
        print(f"Running Go implementation with concurrency {concurrency}...")
        if use_binary_tree:
            # For binary tree, Go expects the flag as the third argument
            cmd = ["./bfs_dfs_go", str(graph_size), str(concurrency), "binary"]
        else:
            cmd = ["./bfs_dfs_go", str(graph_size), str(concurrency)]
            
        run_process = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        
        # Print the output
        output = run_process.stdout
        print(output)
        
        # Parse the Go results
        go_results = {}
        parsing_results = False
        
        for line in output.split('\n'):
            # Check for the results marker
            if '===RESULTS_START===' in line:
                parsing_results = True
                continue
            elif '===RESULTS_END===' in line:
                parsing_results = False
                continue
                
            # Parse the results if we're in the results section
            if parsing_results:
                if line.startswith('bfs:'):
                    time_value = float(line.split(':')[1].strip())
                    go_results['bfs'] = {'time': time_value}
                elif line.startswith('dfs_recursive:'):
                    time_value = float(line.split(':')[1].strip())
                    go_results['dfs_recursive'] = {'time': time_value}
                elif line.startswith('dfs_iterative:'):
                    time_value = float(line.split(':')[1].strip())
                    go_results['dfs_iterative'] = {'time': time_value}
            
            # Also try the old format as a fallback
            elif 'BFS Time:' in line and not 'Visited:' in line:
                parts = line.split(',')
                time_part = parts[0].split(':')[1].strip()
                go_results['bfs'] = {'time': float(time_part.split()[0])}
            elif 'BFS Time:' in line and 'Visited:' in line:
                parts = line.split(',')
                time_part = parts[0].split(':')[1].strip()
                # Extract just the number from "0.002779 seconds"
                time_value = float(time_part.split()[0])
                go_results['bfs'] = {'time': time_value}
            elif 'DFS (Recursive) Time:' in line and not 'Visited:' in line:
                parts = line.split(',')
                time_part = parts[0].split(':')[1].strip()
                go_results['dfs_recursive'] = {'time': float(time_part.split()[0])}
            elif 'DFS (Recursive) Time:' in line and 'Visited:' in line:
                parts = line.split(',')
                time_part = parts[0].split(':')[1].strip()
                # Extract just the number from "0.001381 seconds"
                time_value = float(time_part.split()[0])
                go_results['dfs_recursive'] = {'time': time_value}
            elif 'DFS (Iterative) Time:' in line and not 'Visited:' in line:
                parts = line.split(',')
                time_part = parts[0].split(':')[1].strip()
                go_results['dfs_iterative'] = {'time': float(time_part.split()[0])}
            elif 'DFS (Iterative) Time:' in line and 'Visited:' in line:
                parts = line.split(',')
                time_part = parts[0].split(':')[1].strip()
                # Extract just the number from "0.001472 seconds"
                time_value = float(time_part.split()[0])
                go_results['dfs_iterative'] = {'time': time_value}
        
        return go_results
    except subprocess.CalledProcessError as e:
        print(f"Error with Go implementation: {e}")
        if hasattr(e, 'stdout') and e.stdout:
            print(f"Stdout: {e.stdout}")
        if hasattr(e, 'stderr') and e.stderr:
            print(f"Stderr: {e.stderr}")
        return None
    except FileNotFoundError:
        print("Go is not installed on this system. Skipping Go implementation.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def run_typescript_implementation(graph_size=50000, concurrency=1, use_binary_tree=False):
    """
    Compile and run the TypeScript implementation.
    
    Args:
        graph_size: Number of vertices in the test graph
        concurrency: Number of concurrent searches to run
        use_binary_tree: Whether to use a binary tree instead of the default test graph
        
    Returns:
        Dictionary with benchmark results if successful, None otherwise
    """
    print("\nChecking if Node.js is installed...")
    try:
        # Check if Node.js is installed
        check_node = subprocess.run(
            ["which", "node"],
            check=True,
            capture_output=True,
            text=True
        )
        
        print("\nCompiling TypeScript implementation...")
        # Compile the TypeScript code
        compile_process = subprocess.run(
            ["npx", "tsc"],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Run the compiled TypeScript program
        print(f"Running TypeScript implementation with concurrency {concurrency}...")
        cmd = ["node", "dist/ts_bfs_dfs.js", str(graph_size), str(concurrency)]
        if use_binary_tree:
            cmd.append("binary")
            
        run_process = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        
        # Parse the JSON output from TypeScript
        try:
            result_data = json.loads(run_process.stdout.strip().split('\n')[-1])
            return {
                'bfs_time': result_data['bfs_time'],
                'dfs_iterative_time': result_data['dfs_iterative_time'],
                'dfs_recursive_time': result_data['dfs_recursive_time'],
                'total_time': result_data['total_time']
            }
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            print(f"Error parsing TypeScript output: {e}")
            print(f"Raw output: {run_process.stdout}")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"Error running TypeScript implementation: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return None
    except FileNotFoundError:
        print("Node.js not found. Please install Node.js to run TypeScript benchmarks.")
        return None

def run_benchmarks(graph_size, concurrency_levels):
    """
    Run benchmarks for Python, Go, and TypeScript implementations with different concurrency levels.
    
    Args:
        graph_size: Number of vertices in the test graph
        concurrency_levels: List of concurrency levels to test
        
    Returns:
        Dictionary with benchmark results for each concurrency level
    """
    results = {}
    
    for concurrency in concurrency_levels:
        print(f"\n===== Running Benchmarks with Graph Size {graph_size} and Concurrency {concurrency} =====")
        
        # Run Python implementation
        print("\n----- Running Python Implementation -----")
        start_time = time.time()
        python_result = run_python_benchmark(graph_size, concurrency=concurrency)
        python_total_time = time.time() - start_time
        print(f"Python Total Execution Time: {python_total_time:.10f} seconds")
        
        # Run Go implementation
        print("\n----- Running Go Implementation -----")
        start_time = time.time()
        go_result = run_go_implementation(graph_size, concurrency=concurrency)
        go_total_time = time.time() - start_time
        
        # Run TypeScript implementation
        print("\n----- Running TypeScript Implementation -----")
        start_time = time.time()
        typescript_result = run_typescript_implementation(graph_size, concurrency=concurrency)
        typescript_total_time = time.time() - start_time
        
        # Store results
        results[concurrency] = {
            'python': {
                'results': python_result,
                'total_time': python_total_time
            },
            'go': {
                'results': go_result,
                'total_time': go_total_time
            },
            'typescript': {
                'results': typescript_result,
                'total_time': typescript_total_time
            }
        }
    
    return results

def print_combined_table(results, graph_size):
    """
    Print a combined table with results for all concurrency levels.
    
    Args:
        results: Dictionary with benchmark results for each concurrency level
        graph_size: Number of vertices in the test graph
    """
    concurrency_levels = sorted(results.keys())
    
    print(f"\n===== Combined Performance Results for Graph Size {graph_size} =====")
    
    # Print header
    header = "Concurrency | Language |   BFS Time (s)   | DFS Iter Time (s)   |   DFS Rec Time (s)   |  Total Time (s)  "
    print(header)
    print("-" * len(header))
    
    # Print results for each concurrency level
    for concurrency in concurrency_levels:
        py_results = results[concurrency]['python']
        go_results = results[concurrency]['go']
        ts_results = results[concurrency]['typescript']
        
        # Python results
        py_bfs_time = py_results['results']['bfs']['time']
        py_dfs_iter_time = py_results['results']['dfs_iterative']['time']
        py_dfs_rec_time = "N/A (skipped)"
        py_total_time = py_results['total_time']
        
        print(f"{concurrency:^11} | {'Python':^8} | {py_bfs_time:^15.10f} | {py_dfs_iter_time:^20.10f} | {py_dfs_rec_time:^15} | {py_total_time:^17.10f}")
        
        # Go results (if available)
        if go_results['results']:
            go_bfs_time = go_results['results']['bfs']['time']
            go_dfs_iter_time = go_results['results']['dfs_iterative']['time']
            go_dfs_rec_time = go_results['results']['dfs_recursive']['time']
            go_total_time = go_results['total_time']
            
            print(f"{concurrency:^11} | {'Go':^8} | {go_bfs_time:^15.10f} | {go_dfs_iter_time:^20.10f} | {go_dfs_rec_time:^19.10f} | {go_total_time:^17.10f}")
        
        # TypeScript results (if available)
        if ts_results['results']:
            ts_bfs_time = ts_results['results']['bfs_time']
            ts_dfs_iter_time = ts_results['results']['dfs_iterative_time']
            ts_dfs_rec_time = ts_results['results']['dfs_recursive_time']
            ts_total_time = ts_results['total_time']
            
            print(f"{concurrency:^11} | {'TypeScript':^8} | {ts_bfs_time:^15.10f} | {ts_dfs_iter_time:^20.10f} | {ts_dfs_rec_time:^19.10f} | {ts_total_time:^17.10f}")
        
        # Calculate speedups (Go vs Python)
        if go_results['results'] and py_total_time > 0:
            go_bfs_speedup = py_bfs_time / go_bfs_time if go_bfs_time > 0 else float('inf')
            go_dfs_iter_speedup = py_dfs_iter_time / go_dfs_iter_time if go_dfs_iter_time > 0 else float('inf')
            go_total_speedup = py_total_time / go_total_time
            
            print(f"{concurrency:^11} | {'Go Speedup':^8} | {go_bfs_speedup:^15.2f}x | {go_dfs_iter_speedup:^20.2f}x | {'N/A':^21} | {go_total_speedup:^17.2f}x")
        
        # Calculate speedups (TypeScript vs Python)
        if ts_results['results'] and py_total_time > 0:
            ts_bfs_speedup = py_bfs_time / ts_bfs_time if ts_bfs_time > 0 else float('inf')
            ts_dfs_iter_speedup = py_dfs_iter_time / ts_dfs_iter_time if ts_dfs_iter_time > 0 else float('inf')
            ts_total_speedup = py_total_time / ts_total_time
            
            print(f"{concurrency:^11} | {'TS Speedup':^8} | {ts_bfs_speedup:^15.2f}x | {ts_dfs_iter_speedup:^20.2f}x | {'N/A':^21} | {ts_total_speedup:^17.2f}x")
        
        # Add a separator between concurrency levels
        print("-" * len(header))

def run_binary_tree_benchmark(tree_size=50000, concurrency=1):
    """
    Run benchmarks specifically for the binary tree structure.
    
    Args:
        tree_size: Number of nodes in the binary tree
        concurrency: Number of concurrent searches to run
        
    Returns:
        Dictionary with benchmark results
    """
    print(f"\n===== Running Binary Tree Benchmark with {tree_size} nodes =====")
    print(f"This test compares BFS and DFS performance when searching for the rightmost leaf node.")
    
    # Run Python implementation
    print("\n----- Running Python Implementation on Binary Tree -----")
    start_time = time.time()
    # We'll use the last node (rightmost leaf) as the target for search
    target_node = tree_size - 1
    python_result = run_python_benchmark(tree_size, start_vertex=0, concurrency=concurrency, use_binary_tree=True)
    python_total_time = time.time() - start_time
    print(f"Python Total Execution Time: {python_total_time:.10f} seconds")
    
    # Run Go implementation
    print("\n----- Running Go Implementation on Binary Tree -----")
    start_time = time.time()
    go_result = run_go_implementation(tree_size, concurrency=concurrency, use_binary_tree=True)
    go_total_time = time.time() - start_time
    
    # Run TypeScript implementation
    print("\n----- Running TypeScript Implementation on Binary Tree -----")
    start_time = time.time()
    typescript_result = run_typescript_implementation(tree_size, concurrency=concurrency, use_binary_tree=True)
    typescript_total_time = time.time() - start_time
    
    # Store and return results
    results = {
        'python': {
            'results': python_result,
            'total_time': python_total_time
        },
        'go': {
            'results': go_result,
            'total_time': go_total_time
        },
        'typescript': {
            'results': typescript_result,
            'total_time': typescript_total_time
        }
    }
    
    return results

def main():
    # Default graph size
    graph_size = 50000
    
    # Parse command line arguments if provided
    if len(sys.argv) > 1:
        try:
            size = int(sys.argv[1])
            if size > 0:
                graph_size = size
        except ValueError:
            print(f"Invalid graph size: {sys.argv[1]}. Using default size {graph_size}.")
    
    # Check for binary tree flag
    use_binary_tree = False
    if len(sys.argv) > 2 and sys.argv[2].lower() == "binary":
        use_binary_tree = True
        tree_size = 50000  # Use 50,000 nodes for the binary tree
    
    if use_binary_tree:
        # Run binary tree benchmark with a single thread
        binary_results = run_binary_tree_benchmark(tree_size, concurrency=1)
        
        # Print simple comparison
        print("\n===== Binary Tree Search Performance (50,000 nodes) =====")
        print("Algorithm | Python Time (s) | Go Time (s) | TypeScript Time (s) | Python vs Go | TS vs Go")
        print("-" * 95)
        
        py_bfs = binary_results['python']['results']['bfs']['time']
        go_bfs = binary_results['go']['results']['bfs']['time'] if binary_results['go']['results'] else 0
        ts_bfs = binary_results['typescript']['results']['bfs_time'] if binary_results['typescript']['results'] else 0
        py_go_bfs_ratio = py_bfs / go_bfs if go_bfs > 0 else float('inf')  # Python time / Go time
        ts_go_bfs_ratio = ts_bfs / go_bfs if go_bfs > 0 else float('inf')  # TS time / Go time
        
        py_dfs_iter = binary_results['python']['results']['dfs_iterative']['time']
        go_dfs_iter = binary_results['go']['results']['dfs_iterative']['time'] if binary_results['go']['results'] else 0
        ts_dfs_iter = binary_results['typescript']['results']['dfs_iterative_time'] if binary_results['typescript']['results'] else 0
        py_go_dfs_iter_ratio = py_dfs_iter / go_dfs_iter if go_dfs_iter > 0 else float('inf')  # Python time / Go time
        ts_go_dfs_iter_ratio = ts_dfs_iter / go_dfs_iter if go_dfs_iter > 0 else float('inf')  # TS time / Go time
        
        print(f"BFS       | {py_bfs:^15.10f} | {go_bfs:^10.10f} | {ts_bfs:^18.10f} | {py_go_bfs_ratio:^12.2f}x | {ts_go_bfs_ratio:^8.2f}x")
        print(f"DFS (Iter)| {py_dfs_iter:^15.10f} | {go_dfs_iter:^10.10f} | {ts_dfs_iter:^18.10f} | {py_go_dfs_iter_ratio:^12.2f}x | {ts_go_dfs_iter_ratio:^8.2f}x")
        
        if binary_results['go']['results'] and 'dfs_recursive' in binary_results['go']['results']:
            go_dfs_rec = binary_results['go']['results']['dfs_recursive']['time']
            ts_dfs_rec = binary_results['typescript']['results']['dfs_recursive_time'] if binary_results['typescript']['results'] else 0
            # Python skips recursive DFS, so we can't calculate Python vs Go
            # But we can calculate TypeScript vs Go
            ts_go_dfs_rec_ratio = ts_dfs_rec / go_dfs_rec if go_dfs_rec > 0 else float('inf')  # TS time / Go time
            print(f"DFS (Rec) | {'N/A (skipped)':^15} | {go_dfs_rec:^10.10f} | {ts_dfs_rec:^18.10f} | {'N/A':^12} | {ts_go_dfs_rec_ratio:^8.2f}x")
    else:
        # Concurrency levels to test
        concurrency_levels = [25, 50, 75, 100]
        
        print(f"\n===== BFS and DFS Performance Comparison with Different Concurrency Levels =====")
        print(f"Graph Size: {graph_size}")
        print(f"Concurrency Levels: {concurrency_levels}")
        
        # Run benchmarks for all concurrency levels
        results = run_benchmarks(graph_size, concurrency_levels)
        
        # Print combined table
        print_combined_table(results, graph_size)

if __name__ == "__main__":
    main()