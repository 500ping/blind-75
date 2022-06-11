from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for c in tokens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:
            stack.append(int(c))
    return stack[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
