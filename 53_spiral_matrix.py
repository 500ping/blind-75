from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    lap = 1
    counter = 0
    res = []
    x, y = 0, 0

    while counter != (rows * cols):
        if (0 <= x < rows 
        and 0 <= y < cols
        and (x, y) not in visited):
            res.append(matrix[x][y])
            visited.add((x, y))
        else:
            lap = lap + 1 if lap + 1 < 5 else 1
            counter -= 1

            if lap == 1:
                x += 1
            elif lap == 2:
                y -= 1
            elif lap == 3:
                x -= 1
            elif lap == 4:
                y += 1
            elif lap == 1:
                x += 1

        if lap == 1:
            y += 1
        elif lap == 2:
            x += 1
        elif lap == 3:
            y -= 1
        elif lap == 4:
            x -= 1
        counter += 1

    return res


matrix = [[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]
print(spiralOrder(matrix))
