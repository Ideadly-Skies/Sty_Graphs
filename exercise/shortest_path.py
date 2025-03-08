from collections import deque

def shortest_path(edges, node_A, node_B):
    # graph with adjacency list structure 
    graph = {} 

    # convert edges to adjacency list
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    # bfs strategy
    level = 0
    queue = deque([ (node_A, level) ])
    visited = set()

    # while queue
    while queue:
        node = queue.popleft() # O(1)
        print("node: ", node)
        print("queue: ", queue)

        if node[0] == node_B:
           return node[1] 

        if node[0] in visited:
           continue 
        
        # add node to visited
        visited.add(node[0])

        # add node to visited
        for neighbor in graph[node[0]]:
            if neighbor not in visited:
                queue.append((neighbor, node[1]+1))
    
    return -1
    
if __name__ == "__main__":
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]

    print(shortest_path(edges, 'w', 'z')) # -> 2

    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]

    print(shortest_path(edges, 'y', 'x')) # -> 1

    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]

    print(shortest_path(edges, 'a', 'e')) # -> 3

    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]

    print(shortest_path(edges, 'e', 'c')) # -> 2

    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]

    print(shortest_path(edges, 'b', 'g')) # -> -1