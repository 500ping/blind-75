def isValid(s):
    for _ in range(int(len(s)/2)):
        s = s.replace('()','')
        s = s.replace('[]','')
        s = s.replace('{}','')
    return s == ''


s = "()"
print(isValid(s))