def move_in_matrix(n, directions):
    position = 0
    move_dict = {"right": 1,"down": n,"left": -1}
    for direction in directions:
        move = move_dict.get(direction, 0)
        position += move
        position = max(0, min(position, n*n-1))   
    return position
n = 3
directions = ["right", "down", "left"]
res = move_in_matrix(n, directions)
print(res)