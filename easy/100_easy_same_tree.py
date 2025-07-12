"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

from token import OP
from typing import Optional

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are identical in structure and values.
    
    Intuition:
    I can think of two ways to approach this problem. The first way is to use DFS.
    Compare node.left with node2.left and node.right with node2.right. 
    if node is None just return
    then we want to return 
    node.val == node2.val
    then call the dfs on both left and right nodes.
    we can write a comparison function for two nodes because two nodes are identical
    when their values are the same. 
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    else:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    


def create_tree_from_list(values: list) -> Optional[TreeNode]:
    """
    Helper function to create a binary tree from a list representation.
    None values represent null nodes.
    """
    if not values:
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
    
    # Test case 1: Basic example - identical trees
    test_input_1_p = [1,2,3]
    test_input_1_q = [1,2,3]
    expected_output_1 = True
    root_1_p = create_tree_from_list(test_input_1_p)
    root_1_q = create_tree_from_list(test_input_1_q)
    result_1 = isSameTree(root_1_p, root_1_q)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Basic example - identical trees", passed_1))
    print(f"Test 1: Input p: {test_input_1_p}, Input q: {test_input_1_q}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Different structure
    test_input_2_p = [1,2]
    test_input_2_q = [1,None,2]
    expected_output_2 = False
    root_2_p = create_tree_from_list(test_input_2_p)
    root_2_q = create_tree_from_list(test_input_2_q)
    result_2 = isSameTree(root_2_p, root_2_q)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Different structure", passed_2))
    print(f"Test 2: Input p: {test_input_2_p}, Input q: {test_input_2_q}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Different values
    test_input_3_p = [1,2,1]
    test_input_3_q = [1,1,2]
    expected_output_3 = False
    root_3_p = create_tree_from_list(test_input_3_p)
    root_3_q = create_tree_from_list(test_input_3_q)
    result_3 = isSameTree(root_3_p, root_3_q)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Different values", passed_3))
    print(f"Test 3: Input p: {test_input_3_p}, Input q: {test_input_3_q}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Both trees are empty
    test_input_4_p = []
    test_input_4_q = []
    expected_output_4 = True
    root_4_p = create_tree_from_list(test_input_4_p)
    root_4_q = create_tree_from_list(test_input_4_q)
    result_4 = isSameTree(root_4_p, root_4_q)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Both trees are empty", passed_4))
    print(f"Test 4: Input p: {test_input_4_p}, Input q: {test_input_4_q}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: One tree is empty, other is not
    test_input_5_p = []
    test_input_5_q = [1]
    expected_output_5 = False
    root_5_p = create_tree_from_list(test_input_5_p)
    root_5_q = create_tree_from_list(test_input_5_q)
    result_5 = isSameTree(root_5_p, root_5_q)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: One tree is empty, other is not", passed_5))
    print(f"Test 5: Input p: {test_input_5_p}, Input q: {test_input_5_q}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Single node trees with same value
    test_input_6_p = [5]
    test_input_6_q = [5]
    expected_output_6 = True
    root_6_p = create_tree_from_list(test_input_6_p)
    root_6_q = create_tree_from_list(test_input_6_q)
    result_6 = isSameTree(root_6_p, root_6_q)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Single node trees with same value", passed_6))
    print(f"Test 6: Input p: {test_input_6_p}, Input q: {test_input_6_q}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Single node trees with different values
    test_input_7_p = [5]
    test_input_7_q = [3]
    expected_output_7 = False
    root_7_p = create_tree_from_list(test_input_7_p)
    root_7_q = create_tree_from_list(test_input_7_q)
    result_7 = isSameTree(root_7_p, root_7_q)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Single node trees with different values", passed_7))
    print(f"Test 7: Input p: {test_input_7_p}, Input q: {test_input_7_q}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Complex identical trees
    test_input_8_p = [1,2,3,4,5,6,7]
    test_input_8_q = [1,2,3,4,5,6,7]
    expected_output_8 = True
    root_8_p = create_tree_from_list(test_input_8_p)
    root_8_q = create_tree_from_list(test_input_8_q)
    result_8 = isSameTree(root_8_p, root_8_q)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Complex identical trees", passed_8))
    print(f"Test 8: Input p: {test_input_8_p}, Input q: {test_input_8_q}")
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