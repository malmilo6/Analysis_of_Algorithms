import random
import networkx as nx
import matplotlib.pyplot as plt
import timeit
import numpy as np
import prettytable as pt


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


algorithms = [
    {
        "name": "BFS",
        "algo": lambda G: bfs(G, 0)
    },
    {
        "name": "DFS",
        "algo": lambda G: dfs(G, 0)
    }
]
plt.title('Unbalanced Graph')
plt.xlabel('Number of nodes')
plt.ylabel('T(s)')

for algo in algorithms:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(1, 30):
        start = timeit.default_timer()
        a = i * 10
        G = generate_unbalanced_graph(a, a / 2)
        # G = generate_balanced_graph(a)
        algo["algo"](G)
        end = timeit.default_timer()
        elements.append(a)
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"])

plt.grid()
plt.legend()
plt.show()
