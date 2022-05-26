from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    m = len(image)
    n = len(image[0])
    source = image[sr][sc]

    def tranform(sr, sc):
        if sr < 0 or sr >= m or sc < 0 or sc >= n:
            return

        if image[sr][sc] == newColor or image[sr][sc] != source:
            return

        if image[sr][sc] == source:
            image[sr][sc] = newColor

        tranform(sr - 1, sc) # down
        tranform(sr, sc - 1) # left
        tranform(sr, sc + 1) # right
        tranform(sr + 1, sc) # up

    tranform(sr, sc)

    return image
        


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(floodFill(image, sr, sc, newColor))