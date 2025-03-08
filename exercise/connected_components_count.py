def connected_components_count(graph):
    visited = set() # O(1) lookup and insertion 

    count = 0 
    for node in graph:
        # explore from that node as far as possible
        if explore(graph, node, visited):
            count += 1

    return count 

def explore(graph, current, visited: set):
    # current is visited
    if current in visited:
        return False

    # add current to visited
    visited.add(current)

    # explore neigbor of current node
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    # done exploring
    return True