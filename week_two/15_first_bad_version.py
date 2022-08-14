def isBadVersion(version: int):
    if version >= 4:
        return True


def firstBadVersion(n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = int(left + (right - left)//2)
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        elif not isBadVersion(mid):
            left = mid + 1
        else:
            right = mid - 1


if __name__ == "__main__":
    print(firstBadVersion(5))
