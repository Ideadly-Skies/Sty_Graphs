from collections import deque

def traverse_distance(graph, node, distance):
    # watch the walkthrough video 
    if node in distance:
        return distance[node]

    # max_length longest path
    max_length = 0
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distance)
        if attempt > max_length:
            max_length = attempt

    distance[node] = 1 + max_length
    return distance[node]

def longest_path(graph):
    # dictionary to store node and distance
    distance = {}

    for node in graph:
        # terminal node 
        if graph[node] == []:
            # 0 distance away from itself
            distance[node] = 0

    for node in graph:
        traverse_distance(graph, node, distance)

    return max(distance.values())

if __name__ == "__main__":
    graph = {
        'a': ['c', 'b'],
        'b': ['c'],
        'c': []
    }

    longest_path(graph) # -> 2