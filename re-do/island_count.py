def island_count(grid):
    count = 0; 
    
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            count += DFS(grid, r, c)
            
    return count
     
def DFS(grid, r: int, c: int, visited=set()):
    # check if row and col out of bounds 
    if r < 0 or r >= len(grid):
        return 0 
    if c < 0 or c >= len(grid[0]):
        return 0     
    
    # check if (r, c) in visited
    if grid[r][c] == "W": 
        return 0 
    
    # check if pos in visited 
    if (r, c) in visited:
        return 0 
    visited.add((r,c)) 
    
    # recursive case 
    DFS(grid, r-1, c, visited)
    DFS(grid, r+1, c, visited)
    DFS(grid, r, c+1, visited)
    DFS(grid, r, c-1, visited)  

    # one whole island traversed
    return 1
    
if __name__ == "__main__":
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    print(island_count(grid)) # -> 3