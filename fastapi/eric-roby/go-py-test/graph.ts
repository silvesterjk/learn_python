// TypeScript Graph Implementation for BFS/DFS Performance Testing

export interface Result {
    bfsTime: number;
    dfsIterativeTime: number;
    dfsRecursiveTime: number;
    totalTime: number;
}

export class Graph {
    private adjacencyList: Map<number, number[]>;
    private nodeCount: number;

    constructor(nodeCount: number) {
        this.nodeCount = nodeCount;
        this.adjacencyList = new Map();
        
        // Initialize adjacency list
        for (let i = 0; i < nodeCount; i++) {
            this.adjacencyList.set(i, []);
        }
    }

    addEdge(from: number, to: number): void {
        this.adjacencyList.get(from)?.push(to);
        this.adjacencyList.get(to)?.push(from); // Undirected graph
    }

    getNeighbors(node: number): number[] {
        return this.adjacencyList.get(node) || [];
    }

    getNodeCount(): number {
        return this.nodeCount;
    }

    // Create a random graph
    static createRandomGraph(nodeCount: number): Graph {
        const graph = new Graph(nodeCount);
        const edgeCount = Math.floor(nodeCount * 1.5); // Average degree of 3
        
        for (let i = 0; i < edgeCount; i++) {
            const from = Math.floor(Math.random() * nodeCount);
            const to = Math.floor(Math.random() * nodeCount);
            
            if (from !== to) {
                graph.addEdge(from, to);
            }
        }
        
        return graph;
    }

    // Create a binary tree
    static createBinaryTree(nodeCount: number): Graph {
        const graph = new Graph(nodeCount);
        
        for (let i = 0; i < nodeCount; i++) {
            const leftChild = 2 * i + 1;
            const rightChild = 2 * i + 2;
            
            if (leftChild < nodeCount) {
                graph.addEdge(i, leftChild);
            }
            if (rightChild < nodeCount) {
                graph.addEdge(i, rightChild);
            }
        }
        
        return graph;
    }
}

// BFS Implementation
export function bfs(graph: Graph, startNode: number): number[] {
    const visited = new Set<number>();
    const queue: number[] = [startNode];
    const result: number[] = [];
    
    visited.add(startNode);
    
    while (queue.length > 0) {
        const currentNode = queue.shift()!;
        result.push(currentNode);
        
        for (const neighbor of graph.getNeighbors(currentNode)) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    
    return result;
}

// DFS Iterative Implementation
export function dfsIterative(graph: Graph, startNode: number): number[] {
    const visited = new Set<number>();
    const stack: number[] = [startNode];
    const result: number[] = [];
    
    while (stack.length > 0) {
        const currentNode = stack.pop()!;
        
        if (!visited.has(currentNode)) {
            visited.add(currentNode);
            result.push(currentNode);
            
            // Add neighbors to stack in reverse order to maintain consistent traversal
            const neighbors = graph.getNeighbors(currentNode);
            for (let i = neighbors.length - 1; i >= 0; i--) {
                if (!visited.has(neighbors[i])) {
                    stack.push(neighbors[i]);
                }
            }
        }
    }
    
    return result;
}

// DFS Recursive Implementation
export function dfsRecursive(graph: Graph, startNode: number): number[] {
    const visited = new Set<number>();
    const result: number[] = [];
    
    function dfsHelper(node: number): void {
        visited.add(node);
        result.push(node);
        
        for (const neighbor of graph.getNeighbors(node)) {
            if (!visited.has(neighbor)) {
                dfsHelper(neighbor);
            }
        }
    }
    
    dfsHelper(startNode);
    return result;
}

// Performance measurement function
function measureTime<T>(fn: () => T): [T, number] {
    const start = performance.now();
    const result = fn();
    const end = performance.now();
    return [result, (end - start) / 1000]; // Convert to seconds
}

// Single benchmark run
export function runSingleBenchmark(graph: Graph): Result {
    const startNode = 0;
    
    // Measure BFS
    const [, bfsTime] = measureTime(() => bfs(graph, startNode));
    
    // Measure DFS Iterative
    const [, dfsIterativeTime] = measureTime(() => dfsIterative(graph, startNode));
    
    // Measure DFS Recursive
    const [, dfsRecursiveTime] = measureTime(() => dfsRecursive(graph, startNode));
    
    const totalTime = bfsTime + dfsIterativeTime + dfsRecursiveTime;
    
    return {
        bfsTime,
        dfsIterativeTime,
        dfsRecursiveTime,
        totalTime
    };
}