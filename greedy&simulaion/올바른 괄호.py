def solution(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append(0)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True

    return False