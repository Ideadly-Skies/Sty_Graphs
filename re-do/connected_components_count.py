def connected_components_count(graph):
    visited = set()

    # connected components count
    connected_components_count = 0

    for vertex in graph:
        if DFS(graph, vertex, visited):
            connected_components_count += 1

    # return connected components count
    return connected_components_count

def DFS(graph, node, visited: set):
    if node in visited:
        return False
    
    # add node to visited
    visited.add(node)

    # recursive case 
    for neighbor in graph[node]:
        DFS(graph, neighbor, visited)

    # done traversing all of the neighbors
    return True

if __name__ == "__main__":
    print(connected_components_count({
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    })) # -> 2)