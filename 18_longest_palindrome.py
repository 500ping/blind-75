def longestPalindrome(s: str) -> int:
    c_in_s_unique = set(s)
    counter = 0
    for c in c_in_s_unique:
        c_counter = s.count(c)
        if c_counter % 2 == 0:
            counter += c_counter
        if c_counter > 2 and c_counter % 2 != 0:
            counter += c_counter - 1
    return counter if counter == len(s) else counter + 1


s = "ccc"
print(longestPalindrome(s))