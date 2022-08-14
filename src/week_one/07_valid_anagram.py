from typing import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
