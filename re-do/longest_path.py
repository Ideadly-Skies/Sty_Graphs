def longest_path(graph):
    # distance hash map
    distance = {}
    
    # marking the leaf nodes    
    for node in graph:
        if graph[node] == []:
            distance[node] = 0
    
    for node in graph:
        traverse(graph, node, distance)
    
    return max(distance.values())

def traverse(graph, curr, distance):
    if curr in distance:
        return distance[curr]
    
    largest = 0
    for neighbor in graph[curr]:
        attempt = traverse(graph, neighbor, distance)
        if attempt > largest:
            largest = attempt

    distance[curr] = 1 + largest
    return distance[curr]