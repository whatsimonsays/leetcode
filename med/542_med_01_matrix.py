"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each 
cell.

The distance between two adjacent cells is 1.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1.
- There is at least one 0 in mat.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from typing import List
from collections import deque

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    """
    Find the distance of the nearest 0 for each cell in the matrix.
    
    Intuition:
    [Leave this section empty for student implementation]
    """
    m, n = len(mat), len(mat[0])
    def valid(x, y) -> bool:
        return 0<=x<m and 0<=y<n and mat[x][y] == 1
    
    queue = deque()
    distance = [[0] * n for _ in range(m)]
    seen = set()
    directions = [(0,1), (0, -1), (-1, 0), (1,0)]

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i,j,1))
                seen.add((i,j))
    
    while queue:
        x, y, steps = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append((nx, ny, steps + 1))
                distance[nx][ny] = steps


    return distance

if __name__ == "__main__":
    # Define test cases as tuples: (name, mat, expected)
    test_cases = [
        ("Example 1", [[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]),
        ("Example 2", [[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]]),
        ("Single cell with 0", [[0]], [[0]]),
        ("Single cell with 1", [[1]], [[0]]),
        ("2x2 all zeros", [[0,0],[0,0]], [[0,0],[0,0]]),
        ("2x2 with one 1", [[0,1],[0,0]], [[0,1],[0,0]]),
        ("2x2 with one 0", [[1,1],[1,0]], [[2,1],[1,0]]),
        ("3x3 with center 1", [[1,1,1],[1,0,1],[1,1,1]], [[2,1,2],[1,0,1],[2,1,2]]),
        ("3x3 with corner 0", [[0,1,1],[1,1,1],[1,1,1]], [[0,1,2],[1,2,3],[2,3,4]]),
        ("4x4 complex", [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]),
        ("4x4 with path", [[0,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,0]], [[0,1,2,3],[1,2,3,2],[2,3,2,1],[3,2,1,0]]),
        ("Large matrix", [[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0]], [[0,1,2,3,4],[1,2,3,4,3],[2,3,4,3,2],[3,4,3,2,1],[4,3,2,1,0]]),
        ("All ones except one zero", [[1,1,1],[1,0,1],[1,1,1]], [[2,1,2],[1,0,1],[2,1,2]]),
        ("Multiple zeros", [[0,1,0],[1,1,1],[0,1,0]], [[0,1,0],[1,2,1],[0,1,0]]),
        ("Zigzag pattern", [[0,1,0,1],[1,0,1,0],[0,1,0,1]], [[0,1,0,1],[1,0,1,0],[0,1,0,1]]),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, mat, expected) in enumerate(test_cases, 1):
        result = updateMatrix(mat)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input mat:")
        for row in mat:
            print(f"  {row}")
        print(f"Expected:")
        for row in expected:
            print(f"  {row}")
        print(f"Got:")
        for row in result:
            print(f"  {row}")
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