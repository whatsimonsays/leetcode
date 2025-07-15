"""
There is a bi-directional graph with n vertices, where each vertex is labeled 
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D 
integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional 
edge between vertex ui and vertex vi. Every vertex pair is connected by at most 
one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source 
to vertex destination.

Given edges and the integers n, source, and destination, return true if there 
is a valid path from source to destination, or false otherwise.

Constraints:
- 1 <= n <= 2 * 10^5
- 0 <= edges.length <= 2 * 10^5
- edges[i].length == 2
- 0 <= ui, vi <= n - 1
- ui != vi
- 0 <= source, destination <= n - 1
- There are no duplicate edges.
- There are no self-loops.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

from typing import List, Dict, Set

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

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Determine if there is a valid path from source to destination in the graph.
    
    Intuition:
    [Leave this section empty for student implementation]
    """
    ds = DSU(n)
    for u,v in edges:
        ds.union(u, v)
    return ds.find(source) == ds.find(destination)

if __name__ == "__main__":
    # Define test cases as tuples: (name, n, edges, source, destination, expected)
    test_cases = [
        ("Example 1", 3, [[0,1],[1,2],[2,0]], 0, 2, True),
        ("Example 2", 6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False),
        ("Single node", 1, [], 0, 0, True),
        ("No edges", 3, [], 0, 2, False),
        ("Direct edge exists", 2, [[0,1]], 0, 1, True),
        ("Multiple paths exist", 4, [[0,1],[1,2],[2,3],[0,3]], 0, 3, True),
        ("Disconnected components", 5, [[0,1],[2,3],[3,4]], 0, 4, False),
        ("Large graph with path", 10, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], 0, 9, True),
        ("Large graph without path", 10, [[0,1],[1,2],[2,3],[3,4],[5,6],[6,7],[7,8],[8,9]], 0, 9, False),
        ("Complex graph with cycles", 6, [[0,1],[1,2],[2,0],[2,3],[3,4],[4,5],[5,3]], 0, 5, True)
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, n, edges, source, destination, expected) in enumerate(test_cases, 1):
        result = validPath(n, edges, source, destination)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input: n={n}, edges={edges}, source={source}, destination={destination}")
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