# white: unexplored
# grey: visiting
# black: visited

# complexity: n = # nodes e = # edges
# time: O(e) space: O(n)
def has_cycle(graph):
    visiting = set()
    visited = set()
    for node in graph:
        # cycle detected 
        if cycle_detect(graph, node, visiting, visited):
            return True
    
    # no cycle detected
    return False 
   
def cycle_detect(graph, node, visiting, visited):
    # no cycle detected by this node
    # and it's already visited 
    if node in visited:
        return False 
    
    # we found a node in visiting
    # return False 
    if node in visiting:
        return True
    
    # add node to visiting 
    visiting.add(node)
    
    # begin DFS traversal 
    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True
     
    # remove node from visiting to avoid duplicate
    # traversal 
    visiting.remove(node)
    
    # add that same node to visited
    visited.add(node)