def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                if (char == ')' and stack[-1] != '(') or (char == '}' and stack[-1] != '{') or (char == ']' and stack[-1] != '['):
                    return False

    return len(stack) == 0

if __name__ == "__main__":
    expr = '[]{}()'
    print(areBracketsBalanced(expr))