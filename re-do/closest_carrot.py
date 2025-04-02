from collections import deque

# BFS Implementation
def closest_carrot(grid, starting_row, starting_col):
    visited = set([ (starting_row, starting_col) ])
    queue = deque([ (starting_row, starting_col, 0) ])
    
    # queue DS 
    while queue:
        row, col, distance = queue.popleft()
        
        if grid[row][col] == "C":
            return distance
        
        # allow us to move in 2D direction in here 
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # iterate through each delta 
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            
            pos = (neighbor_row, neighbor_col)
            row_inbounds = 0 <= neighbor_row < len(grid)
            col_inbounds = 0 <= neighbor_col < len(grid[0])
            
            if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != 'X':
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))
    
    # no shortest path found 
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