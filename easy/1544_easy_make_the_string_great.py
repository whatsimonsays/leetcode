def makeGood(self, s: str) -> str:
    stack = []
    for c in s:
        if stack and stack[-1].upper() == c.upper() and stack[-1] != c:
            stack.pop()
        else:
            stack.append(c)
    
    return "".join(stack)


    