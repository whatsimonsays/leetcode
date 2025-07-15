"""
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the tree. You are 
also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting 
a restricted node.

Note that node 0 will not be a restricted node.

Constraints:
- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- edges represents a valid tree.
- 1 <= restricted.length < n
- 1 <= restricted[i] < n
- All values in restricted are unique.

Example 1:
Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4
Explanation: The diagram above shows the tree.
We have that [0,1,2,3] are the only nodes that can be reached from node 0 
without visiting a restricted node.

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
Output: 3
Explanation: The diagram above shows the tree.
We have that [0,5,6] are the only nodes that can be reached from node 0 
without visiting a restricted node.
"""

from typing import List, Set, Dict
from collections import defaultdict, deque

def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    """
    Find the maximum number of nodes reachable from node 0 without visiting 
    restricted nodes.
    
    Intuition:
    DFS, BFS, or DSU.
    """
    ans = 0
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    seen = [False] * n
    for r in restricted:
        seen[r] = True
    
    def dfs(node):
        seen[node] = True
        nonlocal ans
        ans += 1
        for v in graph[node]:
            if not seen[v]:
                dfs(v)
    
    dfs(0)
    return ans

if __name__ == "__main__":
    # Define test cases as tuples: (name, n, edges, restricted, expected)
    test_cases = [
        ("Example 1", 7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5], 4),
        ("Example 2", 7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,2,1], 3),
        ("Single node", 1, [], [], 1),
        ("Two nodes connected", 2, [[0,1]], [], 2),
        ("Two nodes with restriction", 2, [[0,1]], [1], 1),
        ("Linear path", 4, [[0,1],[1,2],[2,3]], [2], 2),
        ("Star graph", 4, [[0,1],[0,2],[0,3]], [1], 3),
        ("Complex tree", 8, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], [3,5], 3),
        ("All nodes reachable", 5, [[0,1],[1,2],[2,3],[3,4]], [], 5),
        ("No nodes reachable", 5, [[0,1],[1,2],[2,3],[3,4]], [1,2,3,4], 1),
        ("Binary tree structure", 7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [1], 4),
        ("Disconnected components", 6, [[0,1],[1,2],[3,4],[4,5]], [3], 3),
        ("Large tree", 10, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], [5], 5),
        ("Multiple restrictions", 6, [[0,1],[1,2],[2,3],[3,4],[4,5]], [2,4], 2),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, n, edges, restricted, expected) in enumerate(test_cases, 1):
        result = reachableNodes(n, edges, restricted)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input: n={n}, edges={edges}, restricted={restricted}")
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