def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    
    return _undirected_graph(graph, node_A, node_B, visited=set()) 
     
def _undirected_graph(graph, node_A, node_B, visited=set()):
    if node_A in visited:
        return
    
    visited.add(node_A) 
     
    if node_A == node_B:
        return True
    
    for neighbor in graph[node_A]:
        if _undirected_graph(graph, neighbor, node_B, visited):
            return True
        
    return False 

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
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]

    print(undirected_path(edges, 'j', 'm')) # -> True
    
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]

    print(undirected_path(edges, 'm', 'j')) # -> True
    
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]

    print(undirected_path(edges, 'l', 'j')) # -> True
    
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]

    print(undirected_path(edges, 'k', 'o')) # -> False