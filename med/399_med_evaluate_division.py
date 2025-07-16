"""
You are given an array of variable pairs equations and an array of real numbers 
values, where equations[i] = [Ai, Bi] and values[i] represent the equation 
Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single 
variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the 
jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, 
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries 
will not result in division by zero and that there is no contradiction.

Constraints:
- 1 <= equations.length <= 20
- equations[i].length == 2
- 1 <= Ai.length, Bi.length <= 5
- values.length == equations.length
- 0.0 < values[i] <= 20.0
- 1 <= queries.length <= 20
- queries[i].length == 2
- 1 <= Cj.length, Dj.length <= 5
- Ai, Bi, Cj, Dj consist of lowercase English letters.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], 
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""

from typing import List, Dict, Set
from collections import defaultdict, deque

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """
    Evaluate division queries based on given equations and values.
    
    Intuition:
    1. build our graph
    2. run dfs over our graph (we only care if a path exists)
    3. return ans
    4. the trick is knowning that AB = X ==> BA = 1/X
    """
    graph = defaultdict(defaultdict)
    for (num, den), value in zip(equations, values):
        graph[num][den] = value
        graph[den][num] = 1/value
    
    def answer_query(start, end):
        if start not in graph:
            return -1

        seen = {start}
        stack = [(start, 1)]

        while stack:
            curr, ratio = stack.pop()
            if curr == end:
                return ratio
            
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append((neighbor, ratio * graph[curr][neighbor]))

        return -1.0
    
    return [answer_query(*query) for query in queries]

if __name__ == "__main__":
    # Define test cases as tuples: (name, equations, values, queries, expected)
    test_cases = [
        ("Example 1", [["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]),
        ("Example 2", [["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]),
        ("Example 3", [["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]], [0.50000,2.00000,-1.00000,-1.00000]),
        ("Single equation", [["x","y"]], [2.0], [["x","y"],["y","x"],["x","x"],["y","y"]], [2.0,0.5,1.0,1.0]),
        ("No equations", [], [], [["a","b"],["x","y"]], [-1.0,-1.0]),
        ("Self division", [["a","b"]], [3.0], [["a","a"],["b","b"]], [1.0,1.0]),
        ("Chain of equations", [["a","b"],["b","c"],["c","d"]], [2.0,3.0,4.0], [["a","d"],["d","a"]], [24.0,0.041666666666666664]),
        ("Disconnected variables", [["a","b"],["c","d"]], [2.0,3.0], [["a","c"],["b","d"],["a","d"]], [-1.0,-1.0,-1.0]),
        ("Large values", [["a","b"],["b","c"]], [1000.0,0.001], [["a","c"],["c","a"]], [1.0,1.0]),
        ("Same variable", [["a","b"]], [2.0], [["a","a"],["b","b"]], [1.0,1.0]),
        ("Complex chain", [["a","b"],["b","c"],["c","d"],["d","e"]], [2.0,3.0,4.0,5.0], [["a","e"],["e","a"]], [120.0,0.008333333333333333]),
        ("Multiple equations same variables", [["a","b"],["a","b"],["b","c"]], [2.0,2.0,3.0], [["a","c"]], [6.0]),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, equations, values, queries, expected) in enumerate(test_cases, 1):
        result = calcEquation(equations, values, queries)
        # Check if results match within small tolerance for floating point
        passed = len(result) == len(expected)
        if passed:
            for r, e in zip(result, expected):
                if abs(r - e) > 1e-5:
                    passed = False
                    break
        
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Equations: {equations}")
        print(f"Values: {values}")
        print(f"Queries: {queries}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
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