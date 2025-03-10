def longest_path(graph):
    # keep track of maximum path length
    max_path_length = 0

    # memoization dictionary to store the longest path for each node
    memo = {}

    for vertex in graph:
        counter = traverse_node(graph, vertex, memo)
        max_path_length = max(max_path_length, counter)

    # return max_path_length
    return max_path_length

def traverse_node(graph, node, memo):
    # return memo 
    if node in memo:
        return memo[node]
   
    # If there are no neighbors, return 0
    if graph[node] == []:
        memo[node] = 0  # No further nodes, so path length is 0
        return 0

    # max counter to hold maximum count variable of a node
    max_counter = 0

    # recursive case: traverse node
    for neighbor in graph[node]:
       # traverse neighbor
       max_counter = max(traverse_node(graph, neighbor, memo), max_counter)

    # store the result for this node in the memo dictionary
    memo[node] = max_counter + 1
    return memo[node] 

if __name__ == "__main__":
    graph = {
        'a': ['c', 'b'],
        'b': ['c'],
        'c': []
    }

    graph = {
        'a': ['c', 'b'],
        'b': ['c'],
        'c': [],
        'q': ['r'],
        'r': ['s', 'u', 't'],
        's': ['t'],
        't': ['u'],
        'u': []
    }

    print(longest_path(graph)) # -> 2