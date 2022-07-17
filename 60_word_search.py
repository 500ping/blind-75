from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited = set()

    def helper(r, c, stage):
        if stage == len(word):
            return True

        if (
                r < 0 or r >= rows 
                or c < 0 or c >= cols 
                or (r, c) in visited
                or board[r][c] != word[stage]
        ):
            return False

        visited.add((r, c))
        res = any(
            [
                helper(r + 1, c, stage+1),
                helper(r - 1, c, stage+1),
                helper(r, c + 1, stage+1),
                helper(r, c - 1, stage+1)
            ]
        )
        visited.remove((r, c))
        return res

    for r in range(rows):
        for c in range(cols):
            if helper(r, c, 0):
                return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
print(exist(board, word))
