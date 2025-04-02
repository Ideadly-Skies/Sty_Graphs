from collections import deque

def best_bridge(grid):
    # locate main_island
    main_island = None 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            attempt = find_island(grid, r, c, set()) 
            if attempt:
                main_island = attempt 
    
    visited = set(main_island)
    queue = deque([])
    for pos in visited:
        r, c = pos
        queue.append((r, c, 0))
        
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'L' and (row, col) not in main_island:
            return distance - 1
        
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            neighbor_pos = (neighbor_row, neighbor_col)
            if is_inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
                visited.add(neighbor_pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))
                
def find_island(grid, r, c, visited):
    # check if out of bound
    if not is_inbounds(grid, r, c) or grid[r][c] == 'W':
        return visited 

    # check if pos in visited
    pos = (r, c)
    if pos in visited:
        return visited
    
    # add pos to visited
    visited.add(pos)
    
    # recursive traversal
    find_island(grid, r+1, c, visited)
    find_island(grid, r-1, c, visited)
    find_island(grid, r, c+1, visited)
    find_island(grid, r, c-1, visited)
    
    # return visited
    return visited 
    
def is_inbounds(grid, r, c):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])
    return row_inbound and col_inbound 
     
if __name__ == "__main__":
    grid = [
        ["W", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "L"],
        ["L", "L", "L", "W", "L"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
    ]
    
    print(best_bridge(grid)) # -> 1