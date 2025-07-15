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
    # Track test results
    test_results = []
    
    # Test case 1: Example 1 from problem
    n_1 = 3
    edges_1 = [[0,1],[1,2],[2,0]]
    source_1 = 0
    destination_1 = 2
    expected_output_1 = True
    result_1 = validPath(n_1, edges_1, source_1, destination_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: n={n_1}, edges={edges_1}, source={source_1}, destination={destination_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    n_2 = 6
    edges_2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source_2 = 0
    destination_2 = 5
    expected_output_2 = False
    result_2 = validPath(n_2, edges_2, source_2, destination_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: n={n_2}, edges={edges_2}, source={source_2}, destination={destination_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Single node (source equals destination)
    n_3 = 1
    edges_3 = []
    source_3 = 0
    destination_3 = 0
    expected_output_3 = True
    result_3 = validPath(n_3, edges_3, source_3, destination_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Single node", passed_3))
    print(f"Test 3: n={n_3}, edges={edges_3}, source={source_3}, destination={destination_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: No edges
    n_4 = 3
    edges_4 = []
    source_4 = 0
    destination_4 = 2
    expected_output_4 = False
    result_4 = validPath(n_4, edges_4, source_4, destination_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: No edges", passed_4))
    print(f"Test 4: n={n_4}, edges={edges_4}, source={source_4}, destination={destination_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Direct edge exists
    n_5 = 2
    edges_5 = [[0,1]]
    source_5 = 0
    destination_5 = 1
    expected_output_5 = True
    result_5 = validPath(n_5, edges_5, source_5, destination_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Direct edge exists", passed_5))
    print(f"Test 5: n={n_5}, edges={edges_5}, source={source_5}, destination={destination_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Multiple paths exist
    n_6 = 4
    edges_6 = [[0,1],[1,2],[2,3],[0,3]]
    source_6 = 0
    destination_6 = 3
    expected_output_6 = True
    result_6 = validPath(n_6, edges_6, source_6, destination_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Multiple paths exist", passed_6))
    print(f"Test 6: n={n_6}, edges={edges_6}, source={source_6}, destination={destination_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Disconnected components
    n_7 = 5
    edges_7 = [[0,1],[2,3],[3,4]]
    source_7 = 0
    destination_7 = 4
    expected_output_7 = False
    result_7 = validPath(n_7, edges_7, source_7, destination_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Disconnected components", passed_7))
    print(f"Test 7: n={n_7}, edges={edges_7}, source={source_7}, destination={destination_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Large graph with path
    n_8 = 10
    edges_8 = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]]
    source_8 = 0
    destination_8 = 9
    expected_output_8 = True
    result_8 = validPath(n_8, edges_8, source_8, destination_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Large graph with path", passed_8))
    print(f"Test 8: n={n_8}, edges={edges_8}, source={source_8}, destination={destination_8}")
    print(f"Expected: {expected_output_8}, Got: {result_8}")
    print(f"Pass: {passed_8}")
    print()
    
    # Test case 9: Large graph without path
    n_9 = 10
    edges_9 = [[0,1],[1,2],[2,3],[3,4],[5,6],[6,7],[7,8],[8,9]]
    source_9 = 0
    destination_9 = 9
    expected_output_9 = False
    result_9 = validPath(n_9, edges_9, source_9, destination_9)
    passed_9 = result_9 == expected_output_9
    test_results.append(("Test 9: Large graph without path", passed_9))
    print(f"Test 9: n={n_9}, edges={edges_9}, source={source_9}, destination={destination_9}")
    print(f"Expected: {expected_output_9}, Got: {result_9}")
    print(f"Pass: {passed_9}")
    print()
    
    # Test case 10: Complex graph with cycles
    n_10 = 6
    edges_10 = [[0,1],[1,2],[2,0],[2,3],[3,4],[4,5],[5,3]]
    source_10 = 0
    destination_10 = 5
    expected_output_10 = True
    result_10 = validPath(n_10, edges_10, source_10, destination_10)
    passed_10 = result_10 == expected_output_10
    test_results.append(("Test 10: Complex graph with cycles", passed_10))
    print(f"Test 10: n={n_10}, edges={edges_10}, source={source_10}, destination={destination_10}")
    print(f"Expected: {expected_output_10}, Got: {result_10}")
    print(f"Pass: {passed_10}")
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