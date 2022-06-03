from tempfile import tempdir


def climbStairs(n: int) -> int:
    # fibonanci
    one, two = 1, 1
    for _ in range(n-1):
        temp = two
        two = one + two
        one = temp
    return two


n = 3
print(climbStairs(n))