import networkx as nx
from heapq import heappush, heappop
import time
import random
import matplotlib.pyplot as plt


def prims_algorithm(graph):
    # Create an empty minimum spanning tree (MST)
    min_spanning_tree = nx.Graph()

    # Get all nodes from the graph
    unvisited_nodes = list(graph.nodes())

    # While there are still nodes that haven't been visited
    while unvisited_nodes:
        # Create an empty heap
        edge_heap = []

        # Pick a start node from the unvisited nodes
        start_node = unvisited_nodes[0]

        # Add the start node to the MST
        min_spanning_tree.add_node(start_node)

        # Add all edges of the start node to the heap
        for edge in graph.edges(start_node, data=True):
            heappush(edge_heap, (edge[2]["weight"], edge[0], edge[1]))

        # Remove the start node from the list of unvisited nodes
        unvisited_nodes.remove(start_node)

        # While there are still edges in the heap
        while edge_heap:
            # Remove edges that connect to visited nodes
            while edge_heap and edge_heap[0][2] not in unvisited_nodes:
                heappop(edge_heap)

            # If there are no more edges in the heap, break the loop
            if not edge_heap:
                break

            # Pop the smallest edge from the heap
            weight, node1, node2 = heappop(edge_heap)

            # Add the smallest edge to the MST
            min_spanning_tree.add_edge(node1, node2, weight=weight)

            # Add all edges of the node just added to the MST to the heap
            for edge in graph.edges(node2, data=True):
                if edge[1] in unvisited_nodes:
                    heappush(edge_heap, (edge[2]["weight"], edge[0], edge[1]))

            # Remove the node just added to the MST from the list of unvisited nodes
            unvisited_nodes.remove(node2)

    return min_spanning_tree


# Kruskal's algorithm
def kruskals_algorithm(graph):
    # Create an empty MST
    min_spanning_tree = nx.Graph()

    # Get a list of all edges in the graph, sorted by weight
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]["weight"])

    # Go through each edge, from smallest to largest
    for edge in sorted_edges:
        # Add the edge to the MST
        min_spanning_tree.add_edge(edge[0], edge[1], weight=edge[2]["weight"])

        # If adding the edge created a cycle, remove it
        if len(list(nx.connected_components(min_spanning_tree))) > 1:
            min_spanning_tree.remove_edge(edge[0], edge[1])

    return min_spanning_tree


# Function to analyze the performance of an algorithm
def analyze_algorithm(algorithm, graph_sizes):
    running_times = []

    for size in graph_sizes:
        graph = nx.gnm_random_graph(size, size * 2, seed=random.randint(0, 100), directed=False)
        nx.set_edge_attributes(graph, {(u, v): {"weight": random.randint(1, 100)} for u, v in graph.edges()})

        start_time = time.time()
        algorithm(graph)
        end_time = time.time()

        running_times.append(end_time - start_time)

    return running_times


graph_sizes = list(range(5, 500, 5))  # Adjust the range of graph sizes as needed

running_times_prims = analyze_algorithm(prims_algorithm, graph_sizes)
running_times_kruskals = analyze_algorithm(kruskals_algorithm, graph_sizes)

plt.plot(graph_sizes, running_times_prims, label="Prim's Algorithm")
plt.grid()
plt.plot(graph_sizes, running_times_kruskals, label="Kruskal's Algorithm")
plt.xlabel("Number of Nodes in Graph")
plt.ylabel("Running Time (s)")
plt.title("Prim's vs Kruskal's Algorithm")
plt.legend()
plt.show()
