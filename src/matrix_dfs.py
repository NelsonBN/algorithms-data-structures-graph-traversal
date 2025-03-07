# Define possible movements: up, right, down, left
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def dfs_maze(maze, start_pos, end_pos):
    # Initialize stack with start position
    stack = [start_pos]

    # Keep track of visited cells and their previous cell for path reconstruction
    visited = {start_pos: None}

    while stack:
        # Pop the last element (DFS uses LIFO - Last In, First Out)
        current = stack.pop()

        # If we reached the end
        if current == end_pos:
            break

        x, y = current

        # Try all four directions
        for dx, dy in DIRECTIONS:
            move_x = x + dy
            move_y = y + dx

            # Check if the new position is valid
            if (0 <= move_y < len(maze) and
                0 <= move_x < len(maze[0]) and
                maze[move_y][move_x] != 'X' and
                (move_x, move_y) not in visited):

                stack.append((move_x, move_y))
                visited[(move_x, move_y)] = current

    # Reconstruct path if end was reached
    if end_pos in visited:
        path = []
        current = end_pos
        while current != start_pos:
            path.append(current)
            current = visited[current]
        path.append(start_pos)
        return path[::-1]  # Reverse to get path from start to end

    return None  # No path found


maze = [
    [' ', ' ', ' ', ' ', 'X'],
    ['S', 'X', ' ', 'X', 'E'],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']]

print("Original Maze:")
for x in maze:
    print(x)

# Find path using DFS
path = dfs_maze(maze, (0, 1), (4, 1))

print("Path found:", path)
print("Path length:", len(path))

# Create a copy of the maze to avoid modifying the original maze
maze_with_path = [row[:] for row in maze]

# Mark the path with '*' except start and end positions
for x, y in path:
    if maze_with_path[y][x] not in ['S', 'E']:
        maze_with_path[y][x] = '*'

print("Maze with path:")
for x in maze_with_path:
    print(x)
