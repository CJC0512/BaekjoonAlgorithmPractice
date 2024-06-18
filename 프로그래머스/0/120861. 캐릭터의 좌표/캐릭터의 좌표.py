def solution(keyinput, board):
    x, y = 0, 0 
    x_limit = (board[0] - 1) // 2
    y_limit = (board[1] - 1) // 2

    for key in keyinput:
        if key == "left":
            x -= 1
        elif key == "right":
            x += 1
        elif key == "up":
            y += 1
        elif key == "down":
            y -= 1

        if x < -x_limit:
            x = -x_limit
        if x > x_limit:
            x = x_limit
        if y < -y_limit:
            y = -y_limit
        if y > y_limit:
            y = y_limit

    return [x, y]