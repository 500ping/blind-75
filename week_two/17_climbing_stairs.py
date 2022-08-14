def climbStairs(n: int) -> int:
    one, two = 1, 1
    for _ in range(n-1):
        temp = two
        two = one + two
        one = temp
    return two


if __name__ == "__main__":
    n = 5
    print(climbStairs(n))
