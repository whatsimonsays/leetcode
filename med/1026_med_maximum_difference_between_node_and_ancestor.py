"""
Given the root of a binary tree, find the maximum value v for which there 
exist different nodes a and b where v = |a.val - b.val| and a is an 
ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b, or 
any child of a is an ancestor of b.

Constraints:
- The number of nodes in the tree is in the range [2, 5000].
- 0 <= Node.val <= 105

Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are 
given below:
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 
1| = 7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3
"""

from optparse import Option
from typing import Optional

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    """
    Find the maximum difference between a node and its ancestor.
    
    Intuition:
    I think we need to keep track of a local minimum and a local maximum. The max diff 
    on one node only would be zero. Lets say all nodes are the same. We would still
    return zero this way. So we basically have four steps:
    1. If we reach a null pointer, return the diff between localmax and local min.
    2/3. Save the value of our helper function as left and right
    4. return the max(left, right)
    """
    if root is None:
        return 0
    
    def helper(root: Optional[TreeNode], localMinimum: int, localMaximum: int) -> int:
        if not root:
            return localMaximum - localMinimum
        localMinimum = min(localMinimum, root.val)
        localMaximum = max(localMaximum, root.val)
        left = helper(root.left, localMinimum, localMaximum)
        right = helper(root.right, localMinimum, localMaximum)

        return max(left, right)
    
    return helper(root, root.val, root.val)


def build_tree(values: list) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a list of values."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

if __name__ == "__main__":
    # Track test results
    test_results = []
    
    # Test case 1: Example 1 from problem
    test_input_1 = [8,3,10,1,6,None,14,None,None,4,7,13]
    expected_output_1 = 7
    root_1 = build_tree(test_input_1)
    result_1 = maxAncestorDiff(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [1,None,2,None,0,3]
    expected_output_2 = 3
    root_2 = build_tree(test_input_2)
    result_2 = maxAncestorDiff(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Simple tree with two nodes
    test_input_3 = [5, 2]
    expected_output_3 = 3
    root_3 = build_tree(test_input_3)
    result_3 = maxAncestorDiff(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Simple two-node tree", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Linear tree (left-skewed)
    test_input_4 = [10, 5, 2, 1]
    expected_output_4 = 9
    root_4 = build_tree(test_input_4)
    result_4 = maxAncestorDiff(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Left-skewed linear tree", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Tree with all same values
    test_input_5 = [5, 5, 5, 5, 5]
    expected_output_5 = 0
    root_5 = build_tree(test_input_5)
    result_5 = maxAncestorDiff(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Tree with all same values", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Complex tree with large differences
    test_input_6 = [100, 50, 200, 25, 75, 150, 250, 10, 30, 60, 80, 125, 175, 225, 275]
    expected_output_6 = 175  # |275 - 100| = 175
    root_6 = build_tree(test_input_6)
    result_6 = maxAncestorDiff(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Complex tree with large differences", passed_6))
    print(f"Test 6: Input: {test_input_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
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