def undirected_path(edges, node_A, node_B, visited=set()):
    # print the value of the current node
    print(node_A)
    
    # derive graph from create_graph function 
    graph = create_graph(edges)

    # no point visiting this node again
    if node_A in visited:
        return False 

    # check if node_A (curr node) is equal to node_B
    if node_A == node_B:
        return True

    # add node to visited list
    visited.add(node_A)
    
    # recursive case 
    for neighbor in graph[node_A]:
        if undirected_path(edges, neighbor, node_B, visited):
            return True          
    
    # no such path exists between node_A and node_B
    return False
        
def create_graph(edges):
    # adjacency list structure
    adjacency_list = {} 
    
    for edge in edges:
        a, b  = edge

        if a not in adjacency_list:
            adjacency_list[a] = []
        if b not in adjacency_list:
            adjacency_list[b] = []
        
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    return adjacency_list

if __name__ == "__main__":
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]

    # return adjacency list
    print(create_graph(edges))

    print(undirected_path(edges, 'j', 'm')) # -> True