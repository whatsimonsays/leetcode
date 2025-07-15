"""
Given an n x n binary matrix grid, return the length of the shortest clear path 
from the top-left corner (0, 0) to the bottom-right corner (n - 1, n - 1). If 
there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) 
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they 
are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2
Explanation: The shortest clear path is shown above.

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Explanation: The shortest clear path is shown above.

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
Explanation: There is no clear path from top-left to bottom-right.
"""

from typing import List
from collections import deque

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    """
    Find the length of the shortest clear path from top-left to bottom-right.
    
    Intuition:
    1. do an initial sanity check on the variables provided
    2. create a helper function that will yield neighbors
    3. BFS approach for this. Make sure to create a seen variable
    """
    # n x n grid
    n = len(grid)
    if not grid or len(grid[0]) == 0 or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    seen = [[False] * n for _ in range(n)]

    def get_neighbors(x, y):
        cardinality = [
            (-1, 1), (0, 1), (1, 1),
            (-1, 0),         (1, 0),
            (-1, -1),(0, -1), (1, -1)
        ]
        for dx, dy in cardinality:
            nx, ny = x + dx, y + dy
            if not((0 <= nx < n) and (0 <= ny < n)):
                continue
            if grid[nx][ny] != 0:
                continue
            yield (nx, ny)

    seen[0][0] = True
    path = 1
    queue = deque([(0,0, path)])
    bottom_right = (n - 1, n - 1)
    while queue:
        x, y, distance = queue.popleft()
        if (x, y) == bottom_right:
            return distance
        for nx, ny in get_neighbors(x, y):
            if seen[nx][ny]:
                continue
            seen[nx][ny] = True
            queue.append((nx, ny, distance + 1))
    
    return -1

if __name__ == "__main__":
    # Define test cases as tuples: (name, grid, expected)
    test_cases = [
        ("Example 1", [[0,1],[1,0]], 2),
        ("Example 2", [[0,0,0],[1,1,0],[1,1,0]], 4),
        ("Example 3", [[1,0,0],[1,1,0],[1,1,0]], -1),
        ("Single cell", [[0]], 1),
        ("Single cell blocked", [[1]], -1),
        ("2x2 all zeros", [[0,0],[0,0]], 2),
        ("2x2 blocked", [[0,1],[1,1]], -1),
        ("3x3 diagonal path", [[0,0,0],[0,1,0],[0,0,0]], 4),
        ("3x3 no path", [[0,0,0],[0,1,1],[0,1,0]], -1),
        ("4x4 clear path", [[0,0,0,0],[1,1,0,0],[0,0,0,1],[0,1,0,0]], 5),
        ("4x4 blocked", [[0,0,0,0],[1,1,1,0],[0,0,0,1],[0,1,0,0]], 6),
        ("Large grid", [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]], 8),
        ("Maze like", [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,1,0,0,0,0],[0,1,0,1,1,0],[0,1,0,0,0,0],[0,0,0,0,0,0]], 10),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, grid, expected) in enumerate(test_cases, 1):
        result = shortestPathBinaryMatrix(grid)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input: grid={grid}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Pass: {passed}")
        print()
    
    # Summary of test results
    passed_tests = [test_name for test_name, passed in test_results if passed]
    failed_tests = [test_name for test_name, passed in test_results if not passed]
    
    print("=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    if failed_tests:
        print(f"❌ {len(failed_tests)} test(s) failed:")
        for test_name in failed_tests:
            print(f"   - {test_name}")
        print(f"✅ {len(passed_tests)} test(s) passed")
    else:
        print(f"✅ All {len(passed_tests)} tests passed!")
    print("=" * 50) 