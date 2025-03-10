def island_count(grid):
    visited = set()

    # island count
    count = 0

    # iterate through the loop O(n^2)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if count_island(grid, r, c, visited):
                count += 1

    # return island_count
    return count 
    
# count island starting from a node
def count_island(grid, r, c, visited: set):
    # check if node is out of bound
    if r < 0 or r >= len(grid):
        return False
    if c < 0 or c >= len(grid[0]):
        return False

    # check if node is visited
    if (r, c) in visited or grid[r][c] == 'W':
        return False
    
    # add node to visited
    visited.add((r, c))

    # recursive case visit left right up and down
    count_island(grid, r-1, c, visited)
    count_island(grid, r+1, c, visited)
    count_island(grid, r, c-1, visited)
    count_island(grid, r, c+1, visited)

    # island visited!
    return True

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