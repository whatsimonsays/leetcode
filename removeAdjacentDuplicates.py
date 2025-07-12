def removeAdjacentDuplicates(s: str):
    """
    Official Answer:
    stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
    """
    if not s:
        return ""
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        else:
            top = stack[-1]
            if c == top:
                stack.pop()
            else:
                stack.append(c)
    
    return "".join(stack)




if __name__ == "__main__":
    test_cases = {
        "abbca" : "aca",
        "abba"  : "",
        "abcd"  : "abcd"
    }
    
    for q, a in test_cases.items():
        assert(a == removeAdjacentDuplicates(q))
    