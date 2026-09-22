def solution(dirs):
    x, y = 0, 0
    paths = []

    move = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }

    for direction in dirs:
        dx, dy = move[direction]
        nx, ny = x + dx, y + dy

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        path = (x, y, nx, ny)
        reverse_path = (nx, ny, x, y)

        if path not in paths and reverse_path not in paths:
            paths.append(path)

        x, y = nx, ny

    return len(paths)

