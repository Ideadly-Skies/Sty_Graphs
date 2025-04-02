def has_path(graph, src, dst, visited=set()):
    # base case 
    if src in visited:
        return
    
    # visit the node
    visited.add(src)
    
    # check if equal to dst
    if src == dst:
        return True
    
    # DFS on neighboring node
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):
            return True
    
    # no path found
    return False 
    
if __name__ == "__main__":
    # graph = {
    #     'f': ['g', 'i'],
    #     'g': ['h'],
    #     'h': [],
    #     'i': ['g', 'k'],
    #     'j': ['i'],
    #     'k': []
    # }

    # print(has_path(graph, 'f', 'k')) # True
    
    # graph = {
    #     'f': ['g', 'i'],
    #     'g': ['h'],
    #     'h': [],
    #     'i': ['g', 'k'],
    #     'j': ['i'],
    #     'k': []
    # }

    # print(has_path(graph, 'f', 'j')) # False
    
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    print(has_path(graph, 'i', 'h')) # True