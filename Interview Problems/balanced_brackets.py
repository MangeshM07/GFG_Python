def areBracketsBalanced(expr):
    stack = []

    # Traversing the expression
    for char in expr:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False

    # If the stack is empty at the end, brackets are balanced
    return len(stack) == 0


if __name__ == "__main__":
    expr = "[()]{}{[()()]()}"
    print(areBracketsBalanced(expr))

    expr = "[(])"
    print(areBracketsBalanced(expr))