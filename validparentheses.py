def isValid(s):
    stack = []
    for x in s:
        if stack:
            if stack[-1] == '[' and x == ']' or stack[-1] == '(' and x == ')' or stack[-1] == '{' and x == '}':
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)
    return len(stack) == 0

print(isValid('()'))