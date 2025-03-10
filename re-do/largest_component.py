from collections import deque

def largest_component(graph):
    visited = set()
    max_size = 0
    
    for vertex in graph:
        max_size = max(BFS(graph, vertex, visited), max_size)
    
    return max_size

def BFS(graph, start_node, visited: set):
    queue = deque( [start_node] )
    visited.add(start_node)
    size = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                size += 1
    
    # return the size of the connected component
    return size

if __name__ == "__main__":
    print(largest_component({
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    })) # -> 4)

    print(largest_component({
        1: [2],
        2: [1,8],
        6: [7],
        9: [8],
        7: [6, 8],
        8: [9, 7, 2]
    })) # -> 6)