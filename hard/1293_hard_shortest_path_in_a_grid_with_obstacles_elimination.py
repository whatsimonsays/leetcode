"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 
1 (obstacle). You can move up, down, left, or right from and to an empty cell in 
one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to 
the lower right corner (m - 1, n - 1) given that you can eliminate at most k 
obstacles. If it is not possible to find such walk return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 40
- 1 <= k <= m * n
- grid[i][j] is either 0 or 1.
- grid[0][0] == grid[m - 1][n - 1] == 0

Example 1:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: The shortest path without eliminating any obstacle is 10. The 
shortest path with one obstacle elimination at position (3,2) is 6. Such path is 
(0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
"""

from typing import List
from collections import deque

def shortestPath(grid: List[List[int]], k: int) -> int:
    """
    Find the minimum number of steps to walk from (0,0) to (m-1,n-1) with at 
    most k obstacle eliminations.
    
    Intuition:
    [Leave this section empty for student implementation]
    """
    m, n = len(grid), len(grid[0])
    def valid(x, y):
        return 0 <= x < m and 0 <= y < n
    
    queue = deque([(0,0,k,0)])
    seen = {(0,0,k)}
    directions = [(0, 1),(0,-1),(-1,0),(1,0)]
    bottom_right = (m - 1, n - 1)
    while queue:
        x, y, remaining, steps = queue.popleft()
        if (x, y) == bottom_right:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid(nx, ny):
                if grid[nx][ny] == 0:
                    if (nx, ny, remaining) not in seen:
                        seen.add((nx,ny,remaining))
                        queue.append((nx, ny, remaining, steps+1))
                elif remaining and (nx, ny, remaining-1) not in seen:
                    seen.add((nx,ny,remaining-1))
                    queue.append((nx, ny, remaining-1, steps+1))

    return -1

if __name__ == "__main__":
    # Define test cases as tuples: (name, grid, k, expected)
    test_cases = [
        ("Example 1", [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1, 6),
        ("Example 2", [[0,1,1],[1,1,1],[1,0,0]], 1, -1),
        ("Single cell", [[0]], 0, 0),
        ("Single cell with obstacle", [[1]], 1, 0),
        ("2x2 with obstacle", [[0,1],[0,0]], 1, 2),
        ("3x3 clear path", [[0,0,0],[0,0,0],[0,0,0]], 0, 4),
        ("3x3 with one obstacle", [[0,0,0],[0,1,0],[0,0,0]], 1, 4),
        ("3x3 with one obstacle no elimination", [[0,0,0],[0,1,0],[0,0,0]], 0, 4),
        ("3x3 blocked path", [[0,1,0],[1,1,1],[0,1,0]], 1, -1),
        ("3x3 blocked path with elimination", [[0,1,0],[1,1,1],[0,1,0]], 2, 4),
        ("Large grid with obstacles", [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]], 0, 14),
        ("All obstacles", [[1,1,1],[1,1,1],[1,1,0]], 8, 4),
        ("Zigzag path", [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]], 4, 6),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, grid, k, expected) in enumerate(test_cases, 1):
        result = shortestPath(grid, k)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input grid:")
        for row in grid:
            print(f"  {row}")
        print(f"k: {k}")
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