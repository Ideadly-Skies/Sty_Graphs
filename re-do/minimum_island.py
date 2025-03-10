from collections import deque

def minimum_island(grid):
    visited = set()
    min_size = float('inf')  # Set min_size to a very large value initially

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # Only start BFS if the current cell is land ('L') and not visited
            if grid[r][c] == 'L' and (r, c) not in visited:
                min_size = min(BFS(grid, r, c, visited), min_size)

    # Return the minimum size of the island
    return min_size if min_size != float('inf') else 0

def BFS(grid, r, c, visited: set):
    # Initialize the queue with the starting tile
    queue = deque([(r, c)])
    visited.add((r, c))
    size = 1  # Start with size 1 for the initial tile

    # BFS algorithm to explore the island
    while queue:
        # Pop from the queue
        current_r, current_c = queue.popleft()

        # Check for 4 possible directions (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = current_r + dr, current_c + dc

            # Only process valid and unvisited land tiles ('L')
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 'L' and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((new_r, new_c))
                size += 1

    # Return the size of the island
    return size