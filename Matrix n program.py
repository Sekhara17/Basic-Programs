def create_matrix(n):
    matrix = [[n * i + j for j in range(n)] for i in range(n)]
    return matrix

def move_in_matrix(n, directions):
    matrix = create_matrix(n)
    x, y = 0, 0  # Start at the top-left corner

    # Direction vectors
    move_dict = {
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
        "up": (-1, 0)
    }
    
    # Process each direction
    for direction in directions:
        dx, dy = move_dict[direction]
        x += dx
        y += dy

        # Ensure x and y stay within matrix bounds
        x = max(0, min(x, n-1))
        y = max(0, min(y, n-1))

    return matrix[x][y]

# Example usage:
n = 3
directions = ["right", "down", "left"]
result = move_in_matrix(n, directions)
print("The value at the final position is:", result)