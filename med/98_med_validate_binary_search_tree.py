"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

from typing import Optional, Any

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    Determine if the binary tree is a valid binary search tree.
    
    Intuition:
    We can do this in o(n) time and space because we will need to visit every node.
    Second: we should keep track of two variables, low and high, that will be our 
    boundaries
    Third do a check that our value lies within our range and return False if 
    this violates that
    Fourth call a function to return left and right
    """
    def validate(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        
        left = validate(node.left, low, node.val)
        right = validate(node.right, node.val, high)
        return left and right
    
    return validate(root, float("-inf"), float("inf"))

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
    
    # Test case 1: Example 1 from problem (valid BST)
    test_input_1 = [2,1,3]
    expected_output_1 = True
    root_1 = build_tree(test_input_1)
    result_1 = isValidBST(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1 - Valid BST", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem (invalid BST)
    test_input_2 = [5,1,4,None,None,3,6]
    expected_output_2 = False
    root_2 = build_tree(test_input_2)
    result_2 = isValidBST(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2 - Invalid BST", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Single node (valid BST)
    test_input_3 = [1]
    expected_output_3 = True
    root_3 = build_tree(test_input_3)
    result_3 = isValidBST(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Single node - Valid BST", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Left child greater than root (invalid BST)
    test_input_4 = [2,3,1]
    expected_output_4 = False
    root_4 = build_tree(test_input_4)
    result_4 = isValidBST(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Left child greater than root - Invalid BST", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Right child less than root (invalid BST)
    test_input_5 = [2,1,1]
    expected_output_5 = False
    root_5 = build_tree(test_input_5)
    result_5 = isValidBST(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Right child less than root - Invalid BST", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Valid BST with multiple levels
    test_input_6 = [10,5,15,3,7,12,18]
    expected_output_6 = True
    root_6 = build_tree(test_input_6)
    result_6 = isValidBST(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Valid BST with multiple levels", passed_6))
    print(f"Test 6: Input: {test_input_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Invalid BST - right subtree has smaller value
    test_input_7 = [10,5,15,3,7,8,20]
    expected_output_7 = False
    root_7 = build_tree(test_input_7)
    result_7 = isValidBST(root_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Invalid BST - right subtree has smaller value", passed_7))
    print(f"Test 7: Input: {test_input_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Invalid BST - left subtree has larger value
    test_input_8 = [10,5,15,3,12,7,18]
    expected_output_8 = False
    root_8 = build_tree(test_input_8)
    result_8 = isValidBST(root_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Invalid BST - left subtree has larger value", passed_8))
    print(f"Test 8: Input: {test_input_8}")
    print(f"Expected: {expected_output_8}, Got: {result_8}")
    print(f"Pass: {passed_8}")
    print()
    
    # Test case 9: Valid BST with negative values
    test_input_9 = [0,-1,1]
    expected_output_9 = True
    root_9 = build_tree(test_input_9)
    result_9 = isValidBST(root_9)
    passed_9 = result_9 == expected_output_9
    test_results.append(("Test 9: Valid BST with negative values", passed_9))
    print(f"Test 9: Input: {test_input_9}")
    print(f"Expected: {expected_output_9}, Got: {result_9}")
    print(f"Pass: {passed_9}")
    print()
    
    # Test case 10: Invalid BST with duplicate values
    test_input_10 = [1,1]
    expected_output_10 = False
    root_10 = build_tree(test_input_10)
    result_10 = isValidBST(root_10)
    passed_10 = result_10 == expected_output_10
    test_results.append(("Test 10: Invalid BST with duplicate values", passed_10))
    print(f"Test 10: Input: {test_input_10}")
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