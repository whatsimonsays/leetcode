"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

1. A single period '.' represents the current directory.
2. A double period '..' represents the previous/parent directory.
3. Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
4. Any sequence of periods that does not match the rules above should be treated as 
a valid directory or file name. For example, '...' and '....' are valid directory or file names.
5. The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.


Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.

"""
def simplifyPath(path: str) -> str:
    if not path or path == "/":
        return "/"
    stack = []
    for dir in path.split("/"):
        if dir in ('', '.'):
            continue
        elif dir == "..":
            if stack:
                stack.pop()
        else:
            stack.append(dir)

    return "/" + "/".join(stack) if stack else "/"

if __name__ == "__main__":
    test_cases = {
        "/home/" : "/home",
        "/home//foo/" : "/home/foo",
        "/home/user/Documents/../Pictures" : "/home/user/Pictures",
        "/../": "/",
        "/.../a/../b/c/../d/./" : "/.../b/d"
    }

    for q, a in test_cases.items():
        assert(a == simplifyPath(q))
