import random
import networkx as nx
import matplotlib.pyplot as plt
import timeit


# Define a function to generate an unbalanced graph with a specified number of nodes and edges
def generate_unbalanced_graph(num_nodes, num_edges):
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i)
    while G.number_of_edges() < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        if node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2)
    return G


def generate_balanced_graph(num_nodes):
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            G.add_edge(i, j)
    return G


# Define a BFS function
def bfs(G, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = [start_node]  # Initialize the queue with the start node
    while queue:
        node = queue.pop(0)  # Get the next node from the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node)  # Print the visited node
            neighbors = G.neighbors(node)  # Get the neighbors of the node
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add the neighbor to the queue


# Define a DFS function
def dfs(G, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)  # Mark the node as visited
    print(start_node)  # Print the visited node
    neighbors = G.neighbors(start_node)  # Get the neighbors of the node
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(G, neighbor, visited)  # Recursively call dfs on the neighbor


# Generate an unbalanced graph with 10 nodes and 15 edges
G_unbalanced = generate_unbalanced_graph(10, 15)
G_balanced = generate_balanced_graph(500)
# Traverse the unbalanced graph using BFS and DFS
start_node = 0
print("BFS:")
bfs(G_unbalanced, start_node)
bfs(G_balanced, start_node)
print("DFS:")
dfs(G_unbalanced, start_node)
dfs(G_balanced, start_node)

# Draw the graph
# pos_unbalanced = nx.spring_layout(G_unbalanced)
# nx.draw_networkx(G_unbalanced, pos=pos_unbalanced)
# plt.show()
#
# pos_balanced = nx.spring_layout(G_balanced)
# nx.draw_networkx(G_balanced, pos=pos_balanced)
# plt.show()
