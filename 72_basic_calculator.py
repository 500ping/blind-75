def calculate(s: str) -> int:
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += signs.pop() * int(s[start:i])
            continue
        if c in '+-(':
            signs += signs[-1] * (1, -1)[c == '-'],
        elif c == ')':
            signs.pop()
        i += 1
    return total


s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))
