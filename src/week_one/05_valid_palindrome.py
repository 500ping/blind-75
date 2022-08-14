def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
