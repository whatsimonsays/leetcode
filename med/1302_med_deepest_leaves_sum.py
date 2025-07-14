"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 100

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Explanation: The deepest leaves are the nodes with values 7 and 8 respectively.
The sum of their values is 7 + 8 = 15.

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
"""

from typing import List, Optional, Any
from collections import deque

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    """
    Find the sum of values of the deepest leaves in the binary tree.
    
    Intuition:
    Same approach as finding the largest value in each row but instead of defining
    a current max for each row, we will just define an empty list and add each value of
    the row we are on. Then when we cant add any more children, that means the final list
    will be the final row of the tree
    """
    if not root:
        return 0
    queue = deque([root])
    while queue:
        res = []
        children = len(queue)
        for _ in range(children):
            curr = queue.popleft()
            res.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    
    return sum(res)

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
    # Track test results
    test_results = []
    
    # Test case 1: Example 1 from problem
    test_input_1 = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    expected_output_1 = 15
    root_1 = build_tree(test_input_1)
    result_1 = deepestLeavesSum(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
    expected_output_2 = 19
    root_2 = build_tree(test_input_2)
    result_2 = deepestLeavesSum(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Single node
    test_input_3 = [5]
    expected_output_3 = 5
    root_3 = build_tree(test_input_3)
    result_3 = deepestLeavesSum(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Single node", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Perfect binary tree
    test_input_4 = [1,2,3,4,5,6,7]
    expected_output_4 = 22  # 4 + 5 + 6 + 7 = 22
    root_4 = build_tree(test_input_4)
    result_4 = deepestLeavesSum(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Perfect binary tree", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Left-skewed tree
    test_input_5 = [1,2,None,3,None,4,None,5]
    expected_output_5 = 5  # Only one deepest leaf
    root_5 = build_tree(test_input_5)
    result_5 = deepestLeavesSum(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Left-skewed tree", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Right-skewed tree
    test_input_6 = [1,None,2,None,3,None,4]
    expected_output_6 = 4  # Only one deepest leaf
    root_6 = build_tree(test_input_6)
    result_6 = deepestLeavesSum(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Right-skewed tree", passed_6))
    print(f"Test 6: Input: {test_input_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Tree with multiple deepest leaves at different depths
    test_input_7 = [1,2,3,4,5,None,6,7,8,9,10,None,None,None,None,11,12,13,14]
    expected_output_7 = 50  # 11 + 12 + 13 + 14 = 50
    root_7 = build_tree(test_input_7)
    result_7 = deepestLeavesSum(root_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Tree with multiple deepest leaves", passed_7))
    print(f"Test 7: Input: {test_input_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Tree with all leaves at same depth
    test_input_8 = [10,5,15,3,7,12,18]
    expected_output_8 = 40  # 3 + 7 + 12 + 18 = 40
    root_8 = build_tree(test_input_8)
    result_8 = deepestLeavesSum(root_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Tree with all leaves at same depth", passed_8))
    print(f"Test 8: Input: {test_input_8}")
    print(f"Expected: {expected_output_8}, Got: {result_8}")
    print(f"Pass: {passed_8}")
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