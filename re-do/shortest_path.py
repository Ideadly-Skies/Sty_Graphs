from collections import deque

def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)

    # init queue and target_paths
    queue = deque([(node_A, 0)])
    target_paths = []

    visited = set()
     
    while queue:
        # pop current element from stack 
        curr, level = queue.popleft() 
        
        # append to target path 
        if curr == node_B:
            target_paths.append((curr, level)) 
            
        # no point visiting same node
        if curr in visited:
            continue
        
        # add current to visited
        visited.add(curr)
     
        # visit neighbor
        for neighbor in graph[curr]:
            queue.append((neighbor, level+1))
         
    return min(target_paths)[1] if target_paths else -1

def build_graph(edges):
    graph = {} 
    
    for edge in edges:
        node1, node2 = edge 
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1) 
         
    return graph

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
    
    edges = [
        ['c', 'n'],
        ['c', 'e'],
        ['c', 's'],
        ['c', 'w'],
        ['w', 'e'],
    ]

    print(shortest_path(edges, 'w', 'e')) # -> 1
    
    edges = [
        ['c', 'n'],
        ['c', 'e'],
        ['c', 's'],
        ['c', 'w'],
        ['w', 'e'],
    ]

    print(shortest_path(edges, 'n', 'e')) # -> 2
    
    edges = [
        ['m', 'n'],
        ['n', 'o'],
        ['o', 'p'],
        ['p', 'q'],
        ['t', 'o'],
        ['r', 'q'],
        ['r', 's']
    ]

    print(shortest_path(edges, 'm', 's')) # -> 6