import matplotlib.pyplot as plt
import networkx as nx

from collections import deque

def shortest_path(edges, node_A, node_B):
    # build adjacency list graph
    graph = build_graph(edges) 
    
    # iterate through each node using BFS
    queue = deque([ (node_A, 0) ]) # init queue with node_A
    visited = set()                # store visited vertices 

    # levels dict to store node and distance to get there
    node_distances = {}

    # iterate through the queue
    while queue:
        # pop from the leftend of the queue
        node, level = queue.popleft()

        # check if node in visited node
        if node in visited:
            continue

        # add node to node_distances
        if node not in node_distances:
            node_distances[node] = [level]
        else:
            node_distances[node].append(level)

        # add node to visited
        visited.add(node)

        # add neighbors to queue
        for neighbor in graph[node]:
            # add neighbor and increment level by 1
            queue.append((neighbor, level+1))
    
    # no such path exists
    if node_B not in node_distances:
        return -1

    # check for minimum levels in here
    return min(node_distances[node_B])

def build_graph(edges):
    # adjacency list we are building
    adjacency_list = {} 
    
    for edge in edges:
        a, b = edge

        if a not in adjacency_list:
            adjacency_list[a] = []
        if b not in adjacency_list:
            adjacency_list[b] = []

        adjacency_list[a].append(b)
        adjacency_list[b].append(a) 

    # return the adjacency list
    return adjacency_list

if __name__ == "__main__":
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]

    # derive node_distances dict from function
    print(shortest_path(edges, 'w', 'z'))

    # build the graph and visualize it
    graph = build_graph(edges)

    # visualize the graph
    # Create graph from adjacency list
    H = nx.Graph(graph)

    # Check nodes in the graph
    print("Nodes in H:", H.nodes)

    # Generate positions using spring layout
    pos = nx.spring_layout(H, seed=42)  # Adding seed for reproducibility

    # Check the positions dictionary
    print("Positions:", pos)

    # Create a figure to plot the graph
    fig = plt.figure(figsize=(12, 4))

    # Draw nodes
    nx.draw_networkx_nodes(H, pos=pos, node_size=200, node_color='w', edgecolors='k')

    # Draw edges
    nx.draw_networkx_edges(H, pos=pos)

    # Draw labels on the nodes
    nx.draw_networkx_labels(H, pos=pos, font_size=12, font_color='black')

    # Display the plot without a box around it
    plt.box(False)

    # Show the plot
    plt.show()