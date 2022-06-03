def isBadVersion(x):
    """
    This function is defined by leetcode
    """
    pass

def firstBadVersion(n: int) -> int:
    low = 1
    high = n 

    while(low <= high):
        mid = int(low + (high - low)//2)
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        elif not isBadVersion(mid):
            low = mid + 1
        else:
            high = mid - 1

    return None


