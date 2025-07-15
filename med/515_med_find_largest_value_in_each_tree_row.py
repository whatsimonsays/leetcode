"""
Given the root of a binary tree, return an array of the largest value in each 
row of the tree (0-indexed).

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]
"""

from typing import List, Optional, Any
from collections import deque

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: Optional[TreeNode]) -> List[int]:
    """
    Find the largest value in each row of the binary tree.
    
    Intuition:
    Straight forward BFS approach. Comes down to five steps:
        1. define a row max value to negative infinity
        2. grab all the nodes on this level
        3. update row max as we iterate on row children
        4. add the children of each node to the queue
        5. append row max to the res list
    """
    if not root:
        return []
    queue = deque([root])
    res = []

    while queue:
        currMax = float("-inf")
        nodes_here: int = len(queue)
        for _ in range(nodes_here):
            curr = queue.popleft()
            currMax = max(currMax, curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(currMax)
    return res

def build_tree(values: List[Any]) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a list of values."""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

if __name__ == "__main__":
    # Define test cases as tuples: (name, tree_values, expected)
    test_cases = [
        ("Example 1", [1,3,2,5,3,None,9], [1,3,9]),
        ("Example 2", [1,2,3], [1,3]),
        ("Single node", [5], [5]),
        ("Left-skewed tree", [10,5,None,3,None,1], [10,5,3,1]),
        ("Right-skewed tree", [1,None,2,None,3,None,4], [1,2,3,4]),
        ("Complex tree with multiple levels", [10,5,15,3,7,12,18,1,4,6,8,11,13,16,20], [10,15,18,20]),
        ("Tree with negative values", [-10,-5,-15,-3,-7,-12,-18], [-10,-5,-3]),
        ("Tree with mixed positive and negative values", [5,-3,8,1,-7,6,9], [5,8,9])
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, tree_values, expected) in enumerate(test_cases, 1):
        root = build_tree(tree_values)
        result = largestValues(root)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input: {tree_values}")
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