"""
You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical). 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, 
return 0.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 
4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
Explanation: There is no island, so we return 0.
"""

from typing import List
from collections import deque

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """
    Find the maximum area of an island in the given grid.
    
    Intuition:
    1. helper function in_bound
    2. a variable named direction holding up down left right directions
    3. a seen 2d array to implement bfs
    4. a variable holding max_area
    5. inside the while loop and before the queue init a current area to 0
    """
    m, n = len(grid), len(grid[0])
    if not grid or n == 0:
        return 0
    def in_bound(x, y):
        return (0 <= x < m) and (0 <= y < n)
    
    dirs = [(0,1), (0,-1), (-1,0), (1,0)] # UP DOWN LEFT RIGHT
    seen = [[False] * n for _ in range(m)] # O(1) lookup and space, no hash
    max_area = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not seen[i][j]:
                seen[i][j] = True
                curr_area = 1
                queue = deque([(i,j)])
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if in_bound(nx, ny) and not seen[nx][ny] and grid[nx][ny] == 1:
                            seen[nx][ny] = True
                            queue.append((nx, ny))
                            curr_area += 1
                max_area = max(max_area, curr_area)
    return max_area

if __name__ == "__main__":
    # Define test cases as tuples: (name, grid, expected)
    test_cases = [
        ("Example 1", [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
        ("Example 2", [[0,0,0,0,0,0,0,0]], 0),
        ("Single island", [[1]], 1),
        ("No islands", [[0,0,0],[0,0,0],[0,0,0]], 0),
        ("Large connected island", [[1,1,1],[1,1,1],[1,1,1]], 9),
        ("Island with hole", [[1,1,1],[1,0,1],[1,1,1]], 8),
        ("Diagonal islands (not connected)", [[1,0,1],[0,1,0],[1,0,1]], 1),
        ("Complex grid", [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]], 4),
        ("Single row with islands", [[1,0,1,0,1]], 1),
        ("Single column with islands", [[1],[0],[1],[0],[1]], 1),
        ("All ones", [[1,1],[1,1]], 4),
        ("All zeros", [[0,0],[0,0]], 0),
        ("Mixed grid", [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 7),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, grid, expected) in enumerate(test_cases, 1):
        result = maxAreaOfIsland(grid)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input grid:")
        for row in grid:
            print(f"  {row}")
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