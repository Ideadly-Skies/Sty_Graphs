# use recursive depth-first traversal
def has_path(graph, src, dst):
    stack = [ src ]

    while stack:
        # set last element as node
        node = stack[-1]
        
        # check if dst exists
        if node == dst:
            return True

        # pop from the end of stack 
        stack.pop()

        # append neighbor to stack
        for neighbor in graph[node]:
            stack.append(neighbor)
    
    # the stack does not contain the dst element
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

    print(has_path(graph, 'i', 'h')) # True