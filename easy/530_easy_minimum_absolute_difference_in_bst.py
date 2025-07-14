"""
Given the root of a Binary Search Tree (BST), return the minimum absolute 
difference between the values of any two different nodes in the tree.

Constraints:
- The number of nodes in the tree is in the range [2, 10^4].
- 0 <= Node.val <= 10^5

Example 1:
Input: root = [4,2,6,1,3]
Output: 1
Explanation: The minimum absolute difference is 1, which is the difference 
between 2 and 1, or between 3 and 2.

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""

from typing import Optional, Any

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    """
    Find the minimum absolute difference between any two different nodes in the BST.
    
    Intuition:
    [Leave this section empty for student implementation]
    """
    if not root:
        return 0
    nodes = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        nodes.append(node.val)
        inorder(node.right)
    
    minimum = float("inf")
    inorder(root)
    for i in range(1, len(nodes)):
        minimum = min(minimum, nodes[i] - nodes[i-1])
    return int(minimum)

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
    # Track test results
    test_results = []
    
    # Test case 1: Example 1 from problem
    test_input_1 = [4,2,6,1,3]
    expected_output_1 = 1
    root_1 = build_tree(test_input_1)
    result_1 = getMinimumDifference(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [1,0,48,None,None,12,49]
    expected_output_2 = 1
    root_2 = build_tree(test_input_2)
    result_2 = getMinimumDifference(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Two nodes with difference 1
    test_input_3 = [5,4]
    expected_output_3 = 1
    root_3 = build_tree(test_input_3)
    result_3 = getMinimumDifference(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Two nodes with difference 1", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Perfect BST with small differences
    test_input_4 = [10,5,15,3,7,12,18]
    expected_output_4 = 2  # 5-3 = 2, 7-5 = 2, 12-10 = 2, 15-12 = 3, etc.
    root_4 = build_tree(test_input_4)
    result_4 = getMinimumDifference(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Perfect BST with small differences", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Left-skewed tree
    test_input_5 = [10,8,None,6,None,4,None,2]
    expected_output_5 = 2  # 2-4 = 2, 4-6 = 2, 6-8 = 2, 8-10 = 2
    root_5 = build_tree(test_input_5)
    result_5 = getMinimumDifference(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Left-skewed tree", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Right-skewed tree
    test_input_6 = [2,None,4,None,6,None,8,None,10]
    expected_output_6 = 2  # 2-4 = 2, 4-6 = 2, 6-8 = 2, 8-10 = 2
    root_6 = build_tree(test_input_6)
    result_6 = getMinimumDifference(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Right-skewed tree", passed_6))
    print(f"Test 6: Input: {test_input_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Large BST with minimum difference at leaves
    test_input_7 = [50,25,75,12,37,62,87,6,18,31,43,56,68,81,93]
    expected_output_7 = 6
    root_7 = build_tree(test_input_7)
    result_7 = getMinimumDifference(root_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Large BST with minimum difference at leaves", passed_7))
    print(f"Test 7: Input: {test_input_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: BST with consecutive values
    test_input_8 = [5,3,7,2,4,6,8]
    expected_output_8 = 1  # 2-3 = 1, 3-4 = 1, 4-5 = 1, 5-6 = 1, 6-7 = 1, 7-8 = 1
    root_8 = build_tree(test_input_8)
    result_8 = getMinimumDifference(root_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: BST with consecutive values", passed_8))
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