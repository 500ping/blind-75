def myAtoi(s: str) -> int:
    MIN = -2**31
    MAX = 2**31 - 1

    s = s.strip()
    result = 0
    is_negative = False

    for i, c in enumerate(s):
        if i == 0 and (c == '+' or c == '-'):
            if c == '-':
                is_negative = True
            continue
        if c.isnumeric():
            result = result * 10 + int(c)
        else:
            break
    
    if is_negative:
        result = -result
    if result < MIN:
        return MIN
    if result > MAX:
        return MAX

    return result


s = "-91283472332"
print(myAtoi(s))
