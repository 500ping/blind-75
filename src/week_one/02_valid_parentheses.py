def isValid(s: str) -> bool:
    stack = []
    symbol_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:
        if char in symbol_dict.values():
            stack.append(char)
        if char in symbol_dict.keys():
            if not stack or symbol_dict[char] != stack.pop():
                return False

    return True


if __name__ == "__main__":
    s = "()"
    print(isValid(s))
