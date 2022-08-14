def longestPalindrome(s: str) -> int:
    uniq_c = set(s)
    result = 0
    for c in uniq_c:
        c_count = s.count(c)
        if c_count % 2 == 0:
            result += c_count
        if c_count > 2 and c_count % 2 != 0:
            result += c_count - 1
    return result if result == len(s) else result + 1


if __name__ == "__main__":
    s = "abccccdd"
    print(longestPalindrome(s))
