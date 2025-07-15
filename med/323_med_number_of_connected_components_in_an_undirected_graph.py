"""
You have a graph of n nodes. You are given an integer n and an array edges where 
edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in 
the graph.

Return the number of connected components in the graph.

Constraints:
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated edges.

Example 1:
Input: n = 4, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation: As shown in the figure above, there are two connected components.

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
Explanation: As shown in the figure above, there is only one connected component.
"""

from typing import List, Dict, Set
from collections import defaultdict, deque

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def countComponents(n: int, edges: List[List[int]]) -> int:
    """
    Count the number of connected components in an undirected graph.
    
    Intuition:
    1. Build a DSU.
    2. Add all the vertices and edges
    3. count the number of parents
    """
    ds = DSU(n)
    for u, v in edges:
        ds.union(u, v)
    return len({ds.find(x) for x in ds.parent})

if __name__ == "__main__":
    # Define test cases as tuples: (name, n, edges, expected)
    test_cases = [
        ("Example 1", 4, [[0,1],[1,2],[3,2]], 1),
        ("Example 2", 5, [[0,1],[1,2],[2,3],[3,4]], 1),
        ("No edges", 3, [], 3),
        ("Single node", 1, [], 1),
        ("Two separate components", 6, [[0,1],[1,2],[3,4],[4,5]], 2),
        ("Three separate components", 9, [[0,1],[1,2],[3,4],[4,5],[6,7],[7,8]], 3),
        ("Isolated nodes with one component", 5, [[0,1],[1,2]], 3),
        ("Complex graph with cycles", 7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]], 2),
        ("Large graph with multiple components", 10, [[0,1],[1,2],[2,3],[4,5],[5,6],[7,8],[8,9]], 3),
        ("All nodes isolated", 5, [], 5)
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, n, edges, expected) in enumerate(test_cases, 1):
        result = countComponents(n, edges)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input: n={n}, edges={edges}")
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