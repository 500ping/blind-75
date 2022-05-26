def isPalindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]



s = "0P"
print(isPalindrome(s))