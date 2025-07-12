def backspace_string_compare(s: str, t: str) -> bool:
    """compare two strings are equal as if they were typed into an editor"""
    def build_stack(a: str):
        stack = []
        for c in a:
            if c != "#":
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build_stack(s) == build_stack(t)

if __name__ == "__main__":
    test_case = {
        ("","") : True,
        ("abc#d", "abb#c#d") : True
    }

    for q, a, in test_case.items():
        first, second = q
        assert(a == backspace_string_compare(first, second))