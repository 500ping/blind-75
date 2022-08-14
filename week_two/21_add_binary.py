from audioop import add


def addBinary(a: str, b: str) -> str:
    s = int(a, 2) + int(b, 2)
    return '{0:b}'.format(s)


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(addBinary(a, b))
