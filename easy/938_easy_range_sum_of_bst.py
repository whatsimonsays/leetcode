"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4].
- 1 <= Node.val <= 10^5
- 1 <= low <= high <= 10^5
- All Node.val are unique.

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""

from typing import Optional, Any

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    
    res = 0
    if low <= root.val <= high:
        res += root.val
    
    if root.val > low:
        res += rangeSumBST(root.left, low, high)
    
    if root.val < high:
        res += rangeSumBST(root.right, low, high)
    
    return res

def build_tree(values: list) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a list of values."""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
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
    # Define test cases as tuples: (name, tree_values, low, high, expected)
    test_cases = [
        ("Example 1", [10,5,15,3,7,None,18], 7, 15, 32),
        ("Example 2", [10,5,15,3,7,13,18,1,None,6], 6, 10, 23),
        ("Single node in range", [5], 3, 7, 5),
        ("Single node not in range", [5], 10, 15, 0),
        ("All nodes in range", [10,5,15,3,7,13,18], 1, 20, 71),
        ("No nodes in range", [10,5,15,3,7,13,18], 20, 25, 0),
        ("Range includes only some nodes", [20,10,30,5,15,25,35], 12, 28, 60),
        ("Large BST with specific range", [50,25,75,12,37,62,87,6,18,31,43,56,68,81,93], 30, 60, 217)
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, tree_values, low, high, expected) in enumerate(test_cases, 1):
        root = build_tree(tree_values)
        result = rangeSumBST(root, low, high)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input: {tree_values}, low={low}, high={high}")
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