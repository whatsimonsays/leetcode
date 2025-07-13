"""
Given a binary tree, find the lowest common ancestor (LCA) of two given 
nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common 
ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a 
descendant of itself)."

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the binary tree.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a 
descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
"""

from typing import Optional

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Find the lowest common ancestor of two nodes in a binary tree.
    
    Intuition:
    theres three cases. 
    ...the base case is that if a node is null meaning we didnt return 
        and we didnt find p or q just return None
    1. First case being that root is p or root is q so we can immediately return root
    because according to the definition of LCA, a node can be its own ancestor.
    2. if p is in the left subtree and q is in the right subtree...
            i.e both calls returned something not null
            i.e we found p and q  then we can immediately return root
    3. since we checked left and right and we didnt return then we just return either left or right
    """
    if root is None:
        return None

    # first case
    if root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # second case
    if left and right:
        return root
    
    # third case
    if left:
        return left
    
    return right

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

def find_node_by_value(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    """
    Helper function to find a node by its value in the tree.
    """
    if root is None:
        return None
    
    if root.val == value:
        return root
    
    left_result = find_node_by_value(root.left, value)
    if left_result:
        return left_result
    
    right_result = find_node_by_value(root.right, value)
    if right_result:
        return right_result
    
    return None

if __name__ == "__main__":
    # Track test results
    test_results = []
    
    # Test case 1: Basic example - LCA is root
    test_input_1 = [3,5,1,6,2,0,8,None,None,7,4]
    p_val_1, q_val_1 = 5, 1
    expected_output_1 = 3
    root_1 = create_tree_from_list(test_input_1)
    p_1 = find_node_by_value(root_1, p_val_1)
    q_1 = find_node_by_value(root_1, q_val_1)
    result_1 = lowestCommonAncestor(root_1, p_1, q_1)
    passed_1 = result_1.val == expected_output_1 if result_1 else False
    test_results.append(("Test 1: Basic example - LCA is root", passed_1))
    print(f"Test 1: Input: {test_input_1}, p={p_val_1}, q={q_val_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1.val if result_1 else None}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: LCA is one of the nodes itself
    test_input_2 = [3,5,1,6,2,0,8,None,None,7,4]
    p_val_2, q_val_2 = 5, 4
    expected_output_2 = 5
    root_2 = create_tree_from_list(test_input_2)
    p_2 = find_node_by_value(root_2, p_val_2)
    q_2 = find_node_by_value(root_2, q_val_2)
    result_2 = lowestCommonAncestor(root_2, p_2, q_2)
    passed_2 = result_2.val == expected_output_2 if result_2 else False
    test_results.append(("Test 2: LCA is one of the nodes itself", passed_2))
    print(f"Test 2: Input: {test_input_2}, p={p_val_2}, q={q_val_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2.val if result_2 else None}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Simple tree with two nodes
    test_input_3 = [1,2]
    p_val_3, q_val_3 = 1, 2
    expected_output_3 = 1
    root_3 = create_tree_from_list(test_input_3)
    p_3 = find_node_by_value(root_3, p_val_3)
    q_3 = find_node_by_value(root_3, q_val_3)
    result_3 = lowestCommonAncestor(root_3, p_3, q_3)
    passed_3 = result_3.val == expected_output_3 if result_3 else False
    test_results.append(("Test 3: Simple tree with two nodes", passed_3))
    print(f"Test 3: Input: {test_input_3}, p={p_val_3}, q={q_val_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3.val if result_3 else None}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: LCA is a leaf node
    test_input_4 = [3,5,1,6,2,0,8,None,None,7,4]
    p_val_4, q_val_4 = 7, 4
    expected_output_4 = 2
    root_4 = create_tree_from_list(test_input_4)
    p_4 = find_node_by_value(root_4, p_val_4)
    q_4 = find_node_by_value(root_4, q_val_4)
    result_4 = lowestCommonAncestor(root_4, p_4, q_4)
    passed_4 = result_4.val == expected_output_4 if result_4 else False
    test_results.append(("Test 4: LCA is a leaf node", passed_4))
    print(f"Test 4: Input: {test_input_4}, p={p_val_4}, q={q_val_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4.val if result_4 else None}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: LCA is deep in the tree
    test_input_5 = [3,5,1,6,2,0,8,None,None,7,4]
    p_val_5, q_val_5 = 6, 0
    expected_output_5 = 3
    root_5 = create_tree_from_list(test_input_5)
    p_5 = find_node_by_value(root_5, p_val_5)
    q_5 = find_node_by_value(root_5, q_val_5)
    result_5 = lowestCommonAncestor(root_5, p_5, q_5)
    passed_5 = result_5.val == expected_output_5 if result_5 else False
    test_results.append(("Test 5: LCA is deep in the tree", passed_5))
    print(f"Test 5: Input: {test_input_5}, p={p_val_5}, q={q_val_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5.val if result_5 else None}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Complex tree with multiple levels
    test_input_6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    p_val_6, q_val_6 = 8, 15
    expected_output_6 = 1
    root_6 = create_tree_from_list(test_input_6)
    p_6 = find_node_by_value(root_6, p_val_6)
    q_6 = find_node_by_value(root_6, q_val_6)
    result_6 = lowestCommonAncestor(root_6, p_6, q_6)
    passed_6 = result_6.val == expected_output_6 if result_6 else False
    test_results.append(("Test 6: Complex tree with multiple levels", passed_6))
    print(f"Test 6: Input: {test_input_6}, p={p_val_6}, q={q_val_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6.val if result_6 else None}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: LCA is in the middle of the tree
    test_input_7 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    p_val_7, q_val_7 = 10, 11
    expected_output_7 = 5
    root_7 = create_tree_from_list(test_input_7)
    p_7 = find_node_by_value(root_7, p_val_7)
    q_7 = find_node_by_value(root_7, q_val_7)
    result_7 = lowestCommonAncestor(root_7, p_7, q_7)
    passed_7 = result_7.val == expected_output_7 if result_7 else False
    test_results.append(("Test 7: LCA is in the middle of the tree", passed_7))
    print(f"Test 7: Input: {test_input_7}, p={p_val_7}, q={q_val_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7.val if result_7 else None}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Edge case - same node
    test_input_8 = [1,2,3]
    p_val_8, q_val_8 = 2, 2
    expected_output_8 = 2
    root_8 = create_tree_from_list(test_input_8)
    p_8 = find_node_by_value(root_8, p_val_8)
    q_8 = find_node_by_value(root_8, q_val_8)
    result_8 = lowestCommonAncestor(root_8, p_8, q_8)
    passed_8 = result_8.val == expected_output_8 if result_8 else False
    test_results.append(("Test 8: Edge case - same node", passed_8))
    print(f"Test 8: Input: {test_input_8}, p={p_val_8}, q={q_val_8}")
    print(f"Expected: {expected_output_8}, Got: {result_8.val if result_8 else None}")
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