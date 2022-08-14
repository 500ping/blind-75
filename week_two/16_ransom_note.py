from typing import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    a_count = Counter(ransomNote)
    b_count = Counter(magazine)

    for key in a_count.keys():
        if b_count.get(key, 0) < a_count.get(key):
            return False
    return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))
