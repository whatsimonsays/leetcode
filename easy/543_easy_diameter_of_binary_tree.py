"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges 
between them.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""

from typing import Optional

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    Find the diameter of a binary tree.
    
    Intuition:
    Stated that the diameter of a tree is the longest path between two nodes on a tree.
    What is a path? A path is the distance between a node and its ancestor leaf. How can
    we modify this to our use case? Hypothesis: If we add the maxDepth of the
    left and right subtrees, we will be given our answer. This was proven false because
    its only half correct. The longest path could not pass through our root, or, the 
    longest path of a node could only be part of the longest path. We need to keep track
    of a diameter variable and update that as we go.
    """
    diameter = 0
    def longestPath(node) -> int:
        if not node:
            return -1
        nonlocal diameter
        left = longestPath(node.left)
        right = longestPath(node.right)
        diameter = max(diameter, left + right + 2)
        return 1 + max(left, right)
        
    longestPath(root)
    return diameter

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
    
    # Test case 1: Example 1 from problem
    test_input_1 = [1,2,3,4,5]
    expected_output_1 = 3
    root_1 = create_tree_from_list(test_input_1)
    result_1 = diameterOfBinaryTree(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [1,2]
    expected_output_2 = 1
    root_2 = create_tree_from_list(test_input_2)
    result_2 = diameterOfBinaryTree(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Single node
    test_input_3 = [1]
    expected_output_3 = 0
    root_3 = create_tree_from_list(test_input_3)
    result_3 = diameterOfBinaryTree(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Single node", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Left-skewed tree
    test_input_4 = [1,2,None,3,None,4]
    expected_output_4 = 3
    root_4 = create_tree_from_list(test_input_4)
    result_4 = diameterOfBinaryTree(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Left-skewed tree", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Right-skewed tree
    test_input_5 = [1,None,2,None,3,None,4]
    expected_output_5 = 3
    root_5 = create_tree_from_list(test_input_5)
    result_5 = diameterOfBinaryTree(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Right-skewed tree", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Balanced tree with diameter through root
    test_input_6 = [1,2,3,4,5,6,7]
    expected_output_6 = 4
    root_6 = create_tree_from_list(test_input_6)
    result_6 = diameterOfBinaryTree(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Balanced tree", passed_6))
    print(f"Test 6: Input: {test_input_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Complex tree with diameter not through root
    test_input_7 = [1,2,3,4,5,None,None,6,7,None,None,None,None,8,9]
    expected_output_7 = 5
    root_7 = create_tree_from_list(test_input_7)
    result_7 = diameterOfBinaryTree(root_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Complex tree", passed_7))
    print(f"Test 7: Input: {test_input_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
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