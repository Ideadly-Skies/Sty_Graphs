def minimum_island(grid):
    """
    Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.
    You may assume that the grid contains at least one island. 
    """
    visited = set()
    
    min_length = float("inf") 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "L" and (r, c) not in visited:
                island_size = explore(grid, r, c, visited)
                min_length = min(island_size, min_length) 
                 
    return min_length 

def explore(grid, r, c, visited):
    # variable to check whether you're out of bounds
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0]) 

    # if either your row and columns are out of bounds
    # return (you've hit the base case)
    if not row_inbounds or not col_inbounds:
        return 0
    
    # print the grid[r][c] entry
    # print("grid[{}][{}] = {}".format(r, c, grid[r][c]))
    
    # check if current entry is a water 
    if grid[r][c] == 'W' or (r, c) in visited:
        return 0

    # add to visited
    visited.add((r, c))

    # look at four neighbor
    size = 1 # current land cell counts as part of the island
    size += explore(grid, r - 1, c, visited)
    size += explore(grid, r + 1, c, visited)
    size += explore(grid, r, c - 1, visited)
    size += explore(grid, r, c + 1, visited)
    # print("size: ", size)

    # done exploring this brand new island
    return size 

if __name__ == "__main__":
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    print(minimum_island(grid)) # -> 2

    grid = [
        ['L', 'W', 'W', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'L', 'L', 'L'],
    ]

    print(minimum_island(grid)) # -> 1

    grid = [
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
    ]

    print(minimum_island(grid)) # -> 9