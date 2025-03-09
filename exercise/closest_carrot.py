from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    # bfs iterative strategy
    level = 0               # represent the path to get to that node 
    queue = deque([ (grid[starting_row][starting_col], level, (starting_row, starting_col)) ])
    visited = set()

    # iterate until we find carrot
    while queue:
        node = queue.popleft()
        print("node: ", node)
        print("queue: ", queue)

        # we have found the carrot
        if node[0] == 'C':
            return node[1]

        # continue iterating if node[0] in visited
        if node[0] in visited:
            continue
        
        # add level to visited
        visited.add(node[2])

        # add neighbor to visited
        r, c = node[2]

        # explore upwards direction 
        if (r - 1) >= 0:
            if ((r-1, c) not in visited and grid[r-1][c] != 'X'):
                queue.append((grid[r-1][c], node[1]+1, (r-1, c)))
        
        # explore downwards direction
        if (r+1) < len(grid):
            if ((r+1, c) not in visited and grid[r+1][c] != 'X'):
                queue.append((grid[r+1][c], node[1]+1, (r+1, c)))
        
        # explore left direction
        if (c-1) >= 0:
            if ((r, c-1) not in visited and grid[r][c-1] != 'X'):
                queue.append((grid[r][c-1], node[1]+1, (r, c-1)))

        # explore right direction
        if (c+1) < len(grid[0]):
            if ((r, c+1) not in visited and grid[r][c+1] != 'X'):
                queue.append((grid[r][c+1], node[1]+1, (r, c+1)))

    # return -1
    return -1

if __name__ == "__main__":
    grid = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'C', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['C', 'O', 'O', 'O', 'O'],
    ]

    print(closest_carrot(grid, 1, 2)) # -> 4

    grid = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'C', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['C', 'O', 'O', 'O', 'O'],
    ]

    print(closest_carrot(grid, 0, 0)) # -> 5

    grid = [
        ['O', 'O', 'X', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'C', 'C', 'O'],
    ]

    print(closest_carrot(grid, 2, 0)) # -> -1