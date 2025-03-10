from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    visited = set()
    queue = deque([(starting_row, starting_col, 0)])  # Store (row, col, distance)
    visited.add((starting_row, starting_col))

    while queue:
        # pop from the front left of queue 
        row, col, distance = queue.popleft()

        # if we found a carrot, return the distance
        if grid[row][col] == 'C':
            return distance

        # Explore the 4 neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = row + dr, col + dc

            # Only process valid and unvisited open spaces ('O')
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != 'X' and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, distance + 1))  # Increment the distance for the next step 

    # if no carrot was found return -1 
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