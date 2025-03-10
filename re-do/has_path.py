def has_path(graph, src, dst):
    # check if src equals destination
    if src == dst:
        return True
    
    # recursive case - handle appropriately
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    
    # no path found with dst node
    return False

if __name__ == "__main__":
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    print(has_path(graph, 'f', 'k')) # True
    print()

    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    print(has_path(graph, 'f', 'j')) # False