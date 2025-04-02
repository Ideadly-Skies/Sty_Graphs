# white grey black algorithm
# white: unexplored
# grey: visiting
# black: visited
def prereqs_possible(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)

    visiting = set() # grey 
    visited = set()  # black
    
    for node in graph:
        # not possible to take all of my courses
        if has_cycle(graph, node, visiting, visited):
            return False
    
    # possible to take all my courses 
    return True

def has_cycle(graph, node, visiting, visited):
    # no point traversing through the same
    # node again 
    if node in visited:
        return False 
    
    # cycle detected 
    if node in visiting:
        return True
    visiting.add(node) 

    # cycle detected
    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visiting, visited):
            return True
    
    # remove node from visiting 
    visiting.remove(node)
    
    # add node to visited
    visited.add(node)   
    return False 
                 
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