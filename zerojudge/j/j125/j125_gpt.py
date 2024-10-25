from collections import deque

def bfs(grid, n, max_diff):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(0, 0)])  # Start from (0, 0)
    visited = set()
    visited.add((0, 0))
    steps = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == n - 1 and y == n - 1:  # Reached bottom-right corner
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if abs(grid[nx][ny] - grid[x][y]) <= max_diff:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        steps += 1
    
    return float('inf')  # If there's no path

def min_max_height_diff(n, heights):
    low, high = 0, max(max(row) for row in heights) - min(min(row) for row in heights)
    best_diff = high
    best_length = float('inf')

    while low <= high:
        mid = (low + high) // 2
        length = bfs(heights, n, mid)
        
        if length < float('inf'):
            best_diff = mid
            best_length = length
            high = mid - 1  # Try to minimize the max height difference
        else:
            low = mid + 1  # Increase the max height difference

    return best_diff, best_length

# Input
n = int(input())
heights = [list(map(int, input().split())) for _ in range(n)]

# Solve the problem
max_height_diff, path_length = min_max_height_diff(n, heights)

# Output
print(max_height_diff)
print(path_length)