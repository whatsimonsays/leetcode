"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root 
node down to the nearest leaf node.

Note: A leaf is a node with no children.

Constraints:
- The number of nodes in the tree is in the range [0, 10^5].
- -1000 <= Node.val <= 1000

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2
Explanation: The minimum depth is 2, which is the path from root (3) to leaf (9).

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
Explanation: The minimum depth is 5, which is the path from root (2) to leaf (6).
"""

from typing import Optional

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    """
    Find the minimum depth of a binary tree.
    
    Intuition:
    [Leave this section empty for student implementation]
    """
    def dfs(root) -> int:
        if root is None:
            return 0
        
        if root.left is None:
            return 1 + dfs(root.right)
        elif root.right is None:
            return 1 + dfs(root.left)
        else:
            return 1 + min(dfs(root.left), dfs(root.right))
    
    return dfs(root)

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
    
    # Test case 1: Basic example
    test_input_1 = [3,9,20,None,None,15,7]
    expected_output_1 = 2
    root_1 = create_tree_from_list(test_input_1)
    result_1 = minDepth(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Basic example", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Skewed tree
    test_input_2 = [2,None,3,None,4,None,5,None,6]
    expected_output_2 = 5
    root_2 = create_tree_from_list(test_input_2)
    result_2 = minDepth(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Skewed tree", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Empty tree
    test_input_3 = []
    expected_output_3 = 0
    root_3 = create_tree_from_list(test_input_3)
    result_3 = minDepth(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Empty tree", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Single node
    test_input_4 = [1]
    expected_output_4 = 1
    root_4 = create_tree_from_list(test_input_4)
    result_4 = minDepth(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Single node", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Balanced tree with minimum depth on left
    test_input_5 = [1,2,3,4,5,6,7,8]
    expected_output_5 = 3
    root_5 = create_tree_from_list(test_input_5)
    result_5 = minDepth(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Balanced tree", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Tree with only left children
    test_input_6 = [1,2,None,3,None,4]
    expected_output_6 = 4
    root_6 = create_tree_from_list(test_input_6)
    result_6 = minDepth(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Left-skewed tree", passed_6))
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