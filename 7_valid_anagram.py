from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    # s = sorted([c for c in s])
    # t = sorted([c for c in t])
    # print(s, t)
    # return s == t

    return Counter(s) == Counter(t)


s = "rat"
t = "car"
print(isAnagram(s, t))


