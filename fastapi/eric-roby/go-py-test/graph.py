# This file defines a graph structure for BFS and DFS algorithms

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, src, dest):
        # Add an edge from src to dest
        self.adj_list[src].append(dest)
    
    def get_adjacency_list(self):
        return self.adj_list
    
    def get_num_vertices(self):
        return self.num_vertices

def create_test_graph(size=1000):
    """
    Creates a test graph with a specified number of vertices.
    The graph is structured to have a mix of short and long paths
    to test both BFS and DFS algorithms effectively.
    """
    g = Graph(size)
    
    # Create a basic structure with some branching
    for i in range(size - 1):
        # Connect to next node (creates a long path)
        g.add_edge(i, i + 1)
        
        # Add some cross connections for every 10th node
        if i % 10 == 0:
            # Connect to nodes further ahead to create shortcuts
            for j in range(1, 6):  # Connect to 5 nodes ahead with varying distances
                if i + j * 10 < size:
                    g.add_edge(i, i + j * 10)
        
        # Add some backward edges for every 20th node
        if i % 20 == 0 and i > 0:
            # Connect back to create cycles
            g.add_edge(i, i // 2)
    
    return g

def create_binary_tree(size=10000):
    """
    Creates a binary tree with the specified number of nodes.
    Each node (except leaf nodes) has exactly two children.
    The rightmost leaf node is the target for search algorithms.
    
    Args:
        size: Number of nodes in the binary tree
        
    Returns:
        Graph object representing a binary tree
    """
    g = Graph(size)
    
    # For a binary tree, each node i has children 2i+1 and 2i+2
    # (except for nodes that would exceed the size)
    for i in range(size):
        # Add left child if within bounds
        left_child = 2 * i + 1
        if left_child < size:
            g.add_edge(i, left_child)
        
        # Add right child if within bounds
        right_child = 2 * i + 2
        if right_child < size:
            g.add_edge(i, right_child)
    
    return g

# Example of how to use the graph
def example_usage():
    # Create a small graph for demonstration
    g = create_test_graph(20)
    
    print("Adjacency List:")
    adj_list = g.get_adjacency_list()
    for i, neighbors in enumerate(adj_list):
        print(f"Vertex {i}: {neighbors}")

if __name__ == "__main__":
    example_usage()