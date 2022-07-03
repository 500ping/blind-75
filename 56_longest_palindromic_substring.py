def longestPalindrome(s: str) -> str:
    longest = ""
    core_start = 0
    s_length = len(s)
    while core_start in range(s_length):
        core_end = core_start

        # identifying the "core"
        while core_end < s_length - 1:
            if s[core_end] == s[core_end + 1]:
                core_end += 1
            else: break

        expand = 0
        # expanding the palindrome left and right
        while (core_start - expand > 0) and (core_end + expand < s_length - 1):
            if s[core_start - expand - 1] == s[core_end + expand + 1]:
                expand += 1
            else: break

        if (core_end + expand + 1) - (core_start - expand) > len(longest):
            longest = s[core_start - expand: core_end + expand + 1]

        # skip through the rest of the "core"
        core_start = core_end + 1

    return longest


s = "aba"
print(longestPalindrome(s))
