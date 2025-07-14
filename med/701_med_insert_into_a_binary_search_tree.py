"""
You are given the root node of a binary search tree (BST) and a value to insert 
into the tree. Return the root node of the BST after the insertion. It is 
guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as 
the tree remains a BST after insertion. You can return any of them.

Constraints:
- The number of nodes in the tree will be in the range [0, 10^4].
- -10^8 <= Node.val <= 10^8
- All the values Node.val are unique.
- -10^8 <= val <= 10^8
- It's guaranteed that val does not exist in the original BST.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is [5,2,7,1,3,null,4].

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
"""

from typing import Optional, Any

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Insert a value into a binary search tree while maintaining BST properties.
    
    Intuition:
    
    """
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
    
    return root

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

def tree_to_list(root: Optional[TreeNode]) -> list:
    """Helper function to convert tree back to list representation for comparison."""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Helper function to validate if the tree is a valid BST."""
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
    
    return validate(root)

if __name__ == "__main__":
    # Track test results
    test_results = []
    
    # Test case 1: Example 1 from problem
    test_input_1 = [4,2,7,1,3]
    val_1 = 5
    expected_output_1 = [4,2,7,1,3,5]  # One possible valid result
    root_1 = build_tree(test_input_1)
    result_1 = insertIntoBST(root_1, val_1)
    result_list_1 = tree_to_list(result_1)
    # Check if result is valid BST and contains the inserted value
    passed_1 = is_valid_bst(result_1) and val_1 in result_list_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}, val={val_1}")
    print(f"Expected: {expected_output_1}, Got: {result_list_1}")
    print(f"Valid BST: {is_valid_bst(result_1)}, Contains {val_1}: {val_1 in result_list_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [40,20,60,10,30,50,70]
    val_2 = 25
    expected_output_2 = [40,20,60,10,30,50,70,None,None,25]  # One possible valid result
    root_2 = build_tree(test_input_2)
    result_2 = insertIntoBST(root_2, val_2)
    result_list_2 = tree_to_list(result_2)
    passed_2 = is_valid_bst(result_2) and val_2 in result_list_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}, val={val_2}")
    print(f"Expected: {expected_output_2}, Got: {result_list_2}")
    print(f"Valid BST: {is_valid_bst(result_2)}, Contains {val_2}: {val_2 in result_list_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Empty tree
    test_input_3 = []
    val_3 = 5
    expected_output_3 = [5]
    root_3 = build_tree(test_input_3)
    result_3 = insertIntoBST(root_3, val_3)
    result_list_3 = tree_to_list(result_3)
    passed_3 = is_valid_bst(result_3) and val_3 in result_list_3
    test_results.append(("Test 3: Empty tree", passed_3))
    print(f"Test 3: Input: {test_input_3}, val={val_3}")
    print(f"Expected: {expected_output_3}, Got: {result_list_3}")
    print(f"Valid BST: {is_valid_bst(result_3)}, Contains {val_3}: {val_3 in result_list_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Single node tree
    test_input_4 = [10]
    val_4 = 5
    expected_output_4 = [10,5]  # Insert as left child
    root_4 = build_tree(test_input_4)
    result_4 = insertIntoBST(root_4, val_4)
    result_list_4 = tree_to_list(result_4)
    passed_4 = is_valid_bst(result_4) and val_4 in result_list_4
    test_results.append(("Test 4: Single node tree", passed_4))
    print(f"Test 4: Input: {test_input_4}, val={val_4}")
    print(f"Expected: {expected_output_4}, Got: {result_list_4}")
    print(f"Valid BST: {is_valid_bst(result_4)}, Contains {val_4}: {val_4 in result_list_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Insert larger value
    test_input_5 = [10]
    val_5 = 15
    expected_output_5 = [10,None,15]  # Insert as right child
    root_5 = build_tree(test_input_5)
    result_5 = insertIntoBST(root_5, val_5)
    result_list_5 = tree_to_list(result_5)
    passed_5 = is_valid_bst(result_5) and val_5 in result_list_5
    test_results.append(("Test 5: Insert larger value", passed_5))
    print(f"Test 5: Input: {test_input_5}, val={val_5}")
    print(f"Expected: {expected_output_5}, Got: {result_list_5}")
    print(f"Valid BST: {is_valid_bst(result_5)}, Contains {val_5}: {val_5 in result_list_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Insert into left subtree
    test_input_6 = [10,5,15]
    val_6 = 3
    expected_output_6 = [10,5,15,3]  # Insert as left child of 5
    root_6 = build_tree(test_input_6)
    result_6 = insertIntoBST(root_6, val_6)
    result_list_6 = tree_to_list(result_6)
    passed_6 = is_valid_bst(result_6) and val_6 in result_list_6
    test_results.append(("Test 6: Insert into left subtree", passed_6))
    print(f"Test 6: Input: {test_input_6}, val={val_6}")
    print(f"Expected: {expected_output_6}, Got: {result_list_6}")
    print(f"Valid BST: {is_valid_bst(result_6)}, Contains {val_6}: {val_6 in result_list_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Insert into right subtree
    test_input_7 = [10,5,15]
    val_7 = 20
    expected_output_7 = [10,5,15,None,None,None,20]  # Insert as right child of 15
    root_7 = build_tree(test_input_7)
    result_7 = insertIntoBST(root_7, val_7)
    result_list_7 = tree_to_list(result_7)
    passed_7 = is_valid_bst(result_7) and val_7 in result_list_7
    test_results.append(("Test 7: Insert into right subtree", passed_7))
    print(f"Test 7: Input: {test_input_7}, val={val_7}")
    print(f"Expected: {expected_output_7}, Got: {result_list_7}")
    print(f"Valid BST: {is_valid_bst(result_7)}, Contains {val_7}: {val_7 in result_list_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Complex BST with deep insertion
    test_input_8 = [50,25,75,12,37,62,87,6,18,31,43,56,68,81,93]
    val_8 = 35
    expected_output_8 = [50,25,75,12,37,62,87,6,18,31,43,56,68,81,93,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,35]
    root_8 = build_tree(test_input_8)
    result_8 = insertIntoBST(root_8, val_8)
    result_list_8 = tree_to_list(result_8)
    passed_8 = is_valid_bst(result_8) and val_8 in result_list_8
    test_results.append(("Test 8: Complex BST with deep insertion", passed_8))
    print(f"Test 8: Input: {test_input_8}, val={val_8}")
    print(f"Expected: {expected_output_8}, Got: {result_list_8}")
    print(f"Valid BST: {is_valid_bst(result_8)}, Contains {val_8}: {val_8 in result_list_8}")
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