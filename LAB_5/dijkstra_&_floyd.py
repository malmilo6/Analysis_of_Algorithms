import networkx as nx
import random
import heapq
import timeit
import matplotlib.pyplot as plt

# Your existing generate_random_weighted_graph function here


def generate_random_weighted_graph(n, p, weight_range):
    # Create a random graph with n nodes and probability p for creating edges
    G = nx.gnp_random_graph(n, p)

    # Assign random weights to the edges within the specified weight range
    for (u, v, w) in G.edges(data=True):
        w['weight'] = random.randint(weight_range[0], weight_range[1])

    return G


def floyd_warshall(graph):
    n = len(graph.nodes)  # Get the number of nodes in the graph
    dist = [[float('inf')]*n for _ in range(n)]  # Initialize the distance matrix with infinite values

    for u in range(n):  # Set the diagonal elements to 0, as the distance from a node to itself is 0
        dist[u][u] = 0

    for u, v, w in graph.edges(data=True):  # Iterate through the edges and fill the distance matrix with weights
        dist[u][v] = w['weight']
        dist[v][u] = w['weight']

    # Apply the Floyd-Warshall algorithm to compute the shortest paths between all pairs of nodes
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist  # Return the distance matrix


def dijkstra(graph, src):
    dist = {node: float('inf') for node in graph.nodes()}  # Initialize the distance dictionary with infinite values
    dist[src] = 0  # Set the distance from the source to itself as 0
    pq = [(0, src)]  # Initialize the priority queue with the source node and distance 0

    while pq:  # Continue until the priority queue is empty
        cur_dist, cur_node = heapq.heappop(pq)  # Pop the node with the smallest distance from the queue

        if cur_dist > dist[cur_node]:  # If the current distance is greater than the recorded distance, skip this
            # iteration
            continue

        # Iterate through the neighbors of the current node and update their distances if necessary
        for neighbor, edge_data in graph[cur_node].items():
            weight = edge_data['weight']
            new_dist = cur_dist + weight

            if new_dist < dist[neighbor]:  # If the new distance is less than the recorded distance, update it
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))  # Push the updated distance and node to the priority queue

    return dist  # Return the distance dictionary



algorithms = [
    {
        "name": "Dijkstra",
        "algo": lambda G: dijkstra(G, 0),
        "color": "b"
    },
    {
        "name": "Floyd Warshall",
        "algo": lambda G: floyd_warshall(G),
        "color": "r"
    }
]

node_weights = [100, 200, 300, 400, 500]

plt.title('')
plt.xlabel('')
plt.ylabel('T(s)')

for algo in algorithms:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(1, 10):
        start = timeit.default_timer()
        a = i * 100
        w_range = (1, a)
        G = generate_random_weighted_graph(1500, 0.3, w_range)
        algo["algo"](G)
        end = timeit.default_timer()
        elements.append(a)
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"], color=algo["color"])

plt.grid()
plt.legend()
plt.show()





