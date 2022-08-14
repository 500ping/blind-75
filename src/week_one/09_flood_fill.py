from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    start_pixel = image[sr][sc]
    visited = set()

    def fill(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
            return
        if image[r][c] != start_pixel:
            return
        image[r][c] == start_pixel
        image[r][c] = color
        visited.add((r, c))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for n_r, n_c in directions:
            fill(r+n_r, c+n_c)

    fill(sr, sc)

    return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    print(floodFill(image, sr, sc, color))
