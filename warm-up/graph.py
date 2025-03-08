from collections import deque

# def depth_first_print(graph, start):
#     # my stack contains the very first node 
#     stack = [ start ]

#     # while stack is not empty
#     while stack:
#         # pop from the top of the stack 
#         current = stack[-1]
#         print(current) 
#         stack.pop()

#         # iterate over the neighbor in the adjacency list
#         for neighbor in graph[current]:
#             stack.append(neighbor)

def depth_first_print(graph, current):
    print(current)

    for neighbor in graph[current]:
        depth_first_print(graph, neighbor)

def breadth_first_print(graph, current):
    queue = deque([ current ])

    while queue:
        node = queue.popleft() # O(1)
        print(node)

        for neighbor in graph[node]:
            queue.append(neighbor)

if __name__ == "__main__":
    # initialize a graph
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }

    # call on the function depth_first_print()
    # depth_first_print(graph, "a")

    # call on the function breadth_first_print()
    breadth_first_print(graph, "a")