from typing import Counter


def minWindow(s: str, t: str) -> str:
    if t == "": 
        return ""

    t_counter = Counter(t)
    window = {}

    have, need = 0, len(t_counter)
    res, res_len = [-1, -1], float('infinity')
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in t_counter and window[c] == t_counter[c]:
            have += 1

        while have == need:
            # update result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1

            window[s[l]] -= 1
            if s[l] in t_counter and window[s[l]] < t_counter[s[l]]:
                have -= 1
            l += 1

    l, r = res

    return s[l: r+1] if res_len != float("infinity") else ""


s = "DAOBECODEBANC"
t = "ABC"
print(minWindow(s, t))