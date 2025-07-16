"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as 
'.') and walls (represented as '+'). You are also given the entrance of the 
maze, where entrance = [entrance_row, entrance_col] denotes the row and column 
of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step 
into a wall and you cannot step outside the maze. Your goal is to find the 
nearest exit from the entrance. An exit is defined as an empty cell that is at 
the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest 
exit, or -1 if no such path exists.

Constraints:
- maze.length == m
- maze[i].length == n
- 1 <= m, n <= 100
- maze[i][j] is either '.' or '+'.
- entrance.length == 2
- 0 <= entrance_row < m
- 0 <= entrance_col < n
- entrance will always be an empty cell.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], 
entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
- You can reach [2,3] by moving 1 step right.
It is impossible to reach [1,0] and [0,2] from the entrance.
Thus, the nearest exit is [2,3], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
"""

from typing import List
from collections import deque

def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    """
    Find the number of steps in the shortest path from entrance to nearest exit.
    
    Intuition:
    0. define our START point
    1. define what an exit is
    2. define helper functions to 
        - determine if a cell is valid
        - determine if a cell is an exit
    3. implement BFS keeping track of a cell, and the steps to that cell
    4. for each neighbor of my current cell, if any of those cells is an exit
        return steps + 1
        mark neighbor as visited
        append neighbor to the queue
    """
    START = tuple(entrance)
    m, n = len(maze), len(maze[0])
    def valid(x, y):
        return 0 <= x < m and 0 <= y < n

    if not maze or n == 0 or not valid(*START):
        return -1

    def is_exit(x, y):
        return (x, y) != START and x == 0 or x == (m - 1) or y == 0 or y == (n - 1)

    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    def get_neighbors(x, y):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and (nx, ny) not in seen and maze[nx][ny] == '.':
                yield (nx, ny)
        
    seen = set()
    queue = deque([])
    seen.add(START)
    x, y = START
    queue.append((x, y, 0))

    while queue:
        i, j, steps = queue.popleft()
        for nx, ny in get_neighbors(i, j):
            if is_exit(nx, ny):
                return steps + 1
            seen.add((nx, ny))
            queue.append((nx, ny, steps + 1))

    return -1

if __name__ == "__main__":
    # Define test cases as tuples: (name, maze, entrance, expected)
    test_cases = [
        ("Example 1", [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2], 1),
        ("Example 2", [["+","+","+"],[".",".","."],["+","+","+"]], [1,0], 2),
        ("Example 3", [[".","+"]], [0,0], -1),
        ("Single cell entrance", [["."]], [0,0], -1),
        ("Single cell wall", [["+"]], [0,0], -1),
        ("2x2 with exit", [[".","."],[".","."]], [0,0], 1),
        ("2x2 blocked", [[".","+"],["+","."]], [0,0], -1),
        ("3x3 center entrance", [[".",".","."],[".",".","."],[".",".","."]], [1,1], 1),
        ("3x3 corner entrance", [[".",".","."],[".",".","."],[".",".","."]], [0,0], 1),
        ("Maze with multiple exits", [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,1], 1),
        ("Large maze", [["."]*10 for _ in range(10)], [5,5], 4),
        ("Entrance at border", [[".",".","."],[".",".","."],[".",".","."]], [0,1], 1),
        ("No path to exit", [["+","+","+"],[".",".","+"],["+","+","+"]], [1,0], -1),
        ("Long path to exit", [["."]*5 for _ in range(5)], [2,2], 2),
        ("Entrance surrounded by walls", [["+","+","+"],["+",".","+"],["+","+","+"]], [1,1], -1),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, maze, entrance, expected) in enumerate(test_cases, 1):
        result = nearestExit(maze, entrance)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input maze:")
        for row in maze:
            print(f"  {row}")
        print(f"Entrance: {entrance}")
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