def largest_component(graph):
    # max size
    max_size = 0 
    
    for node in graph:
        max_size = max(max_size, DFS(graph, node, 0, set()))
        
    return max_size

def DFS(graph, curr, size, visited):
    # base case 
    if curr in visited:
        return 0
    
    # mark visited and increment size 
    visited.add(curr)
    size += 1
     
    for neighbor in graph[curr]:
        size = max(size, DFS(graph, neighbor, size, visited))
    
    return size
        
if __name__ == "__main__":
    # print(largest_component({
    #     0: [8, 1, 5],
    #     1: [0],
    #     5: [0, 8],
    #     8: [0, 5],
    #     2: [3, 4],
    #     3: [2, 4],
    #     4: [3, 2]
    # })) # -> 4
    
    print(largest_component({
        1: [2],
        2: [1,8],
        6: [7],
        9: [8],
        7: [6, 8],
        8: [9, 7, 2]
    })) # -> 6