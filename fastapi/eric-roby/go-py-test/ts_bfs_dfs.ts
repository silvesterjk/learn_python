// TypeScript BFS/DFS Benchmark Runner

import { Graph, Result, runSingleBenchmark } from './graph.js';

// Concurrent benchmark execution
export async function runConcurrentBenchmark(
    graphSize: number,
    concurrency: number,
    useBinaryTree: boolean = false
): Promise<Result> {
    const promises: Promise<Result>[] = [];
    
    // Create concurrent benchmark tasks
    for (let i = 0; i < concurrency; i++) {
        const promise = new Promise<Result>((resolve) => {
            // Create graph for this worker
            const graph = useBinaryTree 
                ? Graph.createBinaryTree(graphSize)
                : Graph.createRandomGraph(graphSize);
            
            // Run benchmark
            const result = runSingleBenchmark(graph);
            resolve(result);
        });
        
        promises.push(promise);
    }
    
    // Wait for all benchmarks to complete
    const results = await Promise.all(promises);
    
    // Calculate average results
    const totalResults = results.reduce(
        (acc, result) => ({
            bfsTime: acc.bfsTime + result.bfsTime,
            dfsIterativeTime: acc.dfsIterativeTime + result.dfsIterativeTime,
            dfsRecursiveTime: acc.dfsRecursiveTime + result.dfsRecursiveTime,
            totalTime: acc.totalTime + result.totalTime
        }),
        { bfsTime: 0, dfsIterativeTime: 0, dfsRecursiveTime: 0, totalTime: 0 }
    );
    
    const count = results.length;
    return {
        bfsTime: totalResults.bfsTime / count,
        dfsIterativeTime: totalResults.dfsIterativeTime / count,
        dfsRecursiveTime: totalResults.dfsRecursiveTime / count,
        totalTime: totalResults.totalTime / count
    };
}

// Main benchmark function that matches the Go/Python interface
export async function runTsBenchmark(
    graphSize: number,
    concurrency: number,
    useBinaryTree: boolean = false
): Promise<Result> {
    return await runConcurrentBenchmark(graphSize, concurrency, useBinaryTree);
}

// CLI interface for standalone execution
if (process.argv[1] && process.argv[1].endsWith('ts_bfs_dfs.js')) {
    async function main() {
        const args = process.argv.slice(2);
        
        if (args.length < 2) {
            console.error('Usage: node ts_bfs_dfs.js <graph_size> <concurrency> [binary]');
            process.exit(1);
        }
        
        const graphSize = parseInt(args[0]);
        const concurrency = parseInt(args[1]);
        const useBinaryTree = args.length > 2 && args[2].toLowerCase() === 'binary';
        
        if (isNaN(graphSize) || isNaN(concurrency)) {
            console.error('Graph size and concurrency must be valid numbers');
            process.exit(1);
        }
        
        try {
            console.log(`Running TypeScript benchmark: ${graphSize} nodes, ${concurrency} concurrent executions`);
            console.log(`Graph type: ${useBinaryTree ? 'Binary Tree' : 'Random Graph'}`);
            
            const result = await runTsBenchmark(graphSize, concurrency, useBinaryTree);
            
            // Output results in JSON format for easy parsing
            console.log(JSON.stringify({
                bfs_time: result.bfsTime,
                dfs_iterative_time: result.dfsIterativeTime,
                dfs_recursive_time: result.dfsRecursiveTime,
                total_time: result.totalTime
            }));
        } catch (error) {
            console.error('Benchmark failed:', error);
            process.exit(1);
        }
    }
    
    main();
}