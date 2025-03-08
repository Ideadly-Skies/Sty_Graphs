from collections import deque

def undirected_path(edges, node_A, node_B):
    # adjacency list structure 
    graph = {}
    
    # convert the graph into an adjacency list
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    queue = deque([node_A])
    visited = set()
    while queue:
        node = queue.popleft() # O(1)

        if node == node_B:
            return True
        
        if node in visited:
            return False

        # add node to visited 
        visited.add(node)

        # add neighbor to queue 
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False