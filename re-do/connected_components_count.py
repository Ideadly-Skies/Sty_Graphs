def connected_components_count(graph):
    count = 0 
    for node in graph:
        count += DFS(graph, node)
    return count
    
def DFS(graph, curr, visited=set()):
    # no point visiting this again 
    if curr in visited:
        return 0
    
    # add curr to visited
    visited.add(curr)
    
    # visit each neighbor 
    for neighbor in graph[curr]:
        DFS(graph, neighbor, visited)
        
    # visitied one component
    return 1

if __name__ == "__main__":
    # print(connected_components_count({
    #     0: [8, 1, 5],
    #     1: [0],
    #     5: [0, 8],
    #     8: [0, 5],
    #     2: [3, 4],
    #     3: [2, 4],
    #     4: [3, 2]
    # })) # -> 2
    
    print(connected_components_count({
        1: [2],
        2: [1,8],
        6: [7],
        9: [8],
        7: [6, 8],
        8: [9, 7, 2]
    })) # -> 1