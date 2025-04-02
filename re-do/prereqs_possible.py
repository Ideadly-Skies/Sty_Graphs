# white grey black algorithm
# white: unexplored
# grey: visiting
# black: visited
def prereqs_possible(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)

    visiting = set() # grey 
    visited = set()  # black
    
    for node in graph:
        # prereqs not possible 
        if has_cycle(graph, node, visiting, visited):
            return False
    
    # prereqs possible 
    return True

def has_cycle(graph, node, visiting, visited):
    # same node already visited and
    # detects no cycle 
    if node in visited:
        return False
    
    # cycle detected 
    if node in visiting:
        return True
    
    # add node to visiting
    visiting.add(node) 
     
    # run DFS on neighbor 
    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visiting, visited):
            return True
    
    # remove node from visiting to
    # to avoid re-traversal  
    visiting.remove(node)
    
    # add node to visited
    visited.add(node)

def build_graph(num_courses, prereqs):
    graph = {}
    for i in range(num_courses):
        graph[i] = []
        
    for prereq in prereqs:
        course_a, course_b = prereq
        graph[course_a].append(course_b)  

    return graph

if __name__ == "__main__":
    numCourses = 6
    prereqs = [
    (0, 1),
    (2, 3),
    (0, 2),
    (1, 3),
    (4, 5),
    ]
    
    print(prereqs_possible(numCourses, prereqs)) # -> True