def minimum_island(grid):
    min_island_size = float("inf")
     
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            size = DFS(grid, r, c)
            if size:
                min_island_size = min(size, min_island_size)
    
    return min_island_size 
             
def DFS(grid, r, c, visited=set()):
    # boundary checking 
    if r < 0 or r >= len(grid):
        return 0
    if c < 0 or c >= len(grid[r]):
        return 0
    
    # edge case checking 
    if grid[r][c] == "W":
        return 0
    
    # update visited set 
    if (r, c) in visited:
        return 0
    visited.add((r, c))
    
    # recursive case
    up_count = DFS(grid, r, c+1, visited)
    down_count = DFS(grid, r, c-1, visited)
    left_count = DFS(grid, r-1, c, visited)
    right_count = DFS(grid, r+1, c, visited)
    
    # count number of land tiles (including this one)
    return 1 + up_count + down_count + left_count + right_count

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