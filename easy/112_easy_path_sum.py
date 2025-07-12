"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

from token import OP
from typing import Optional

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    Check if there exists a root-to-leaf path with sum equal to targetSum.
    
    Intuition: Use DFS to go down the tree. If we reach a null pointer return false and go back up a level. This handles the base case. Now we subtract the root value from the targetSum and save as newTarget. if both the left and right children are null pointers, return newTarget == 0. Otherwise, recurse on the left child as left and the right child  as right and return left or right.
    """
    if root is None:
        return False
    
    target = targetSum - root.val
    if root.left is None and root.right is None:
        return target == 0
    left = hasPathSum(root.left, target)
    right = hasPathSum(root.right, target)

    return left or right

def hasPathSumIterative(root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False

    stack = [(root, 0)]
    while stack:
        node, currentSum = stack.pop()
        currentSum = currentSum + node.val
        if node.left is None and node.right is None:
            if currentSum == targetSum:
                return True
        if node.left:
            stack.append((node.left, currentSum))
        if node.right:
            stack.append((node.right, currentSum))
    
    return False


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
    # Test case 1: Basic example with path sum = 22
    test_input_1 = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    target_sum_1 = 22
    expected_output_1 = True
    root_1 = create_tree_from_list(test_input_1)
    result_1 = hasPathSum(root_1, target_sum_1)
    print(f"Test 1: Input: {test_input_1}, Target Sum: {target_sum_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {result_1 == expected_output_1}")
    print()
    
    # Test case 2: No path with sum = 5
    test_input_2 = [1,2,3]
    target_sum_2 = 5
    expected_output_2 = False
    root_2 = create_tree_from_list(test_input_2)
    result_2 = hasPathSum(root_2, target_sum_2)
    print(f"Test 2: Input: {test_input_2}, Target Sum: {target_sum_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {result_2 == expected_output_2}")
    print()
    
    # Test case 3: Empty tree
    test_input_3 = []
    target_sum_3 = 0
    expected_output_3 = False
    root_3 = create_tree_from_list(test_input_3)
    result_3 = hasPathSum(root_3, target_sum_3)
    print(f"Test 3: Input: {test_input_3}, Target Sum: {target_sum_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {result_3 == expected_output_3}")
    print()
    
    # Test case 4: Single node tree with matching sum
    test_input_4 = [5]
    target_sum_4 = 5
    expected_output_4 = True
    root_4 = create_tree_from_list(test_input_4)
    result_4 = hasPathSum(root_4, target_sum_4)
    print(f"Test 4: Input: {test_input_4}, Target Sum: {target_sum_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {result_4 == expected_output_4}")
    print()
    
    # Test case 5: Single node tree with non-matching sum
    test_input_5 = [5]
    target_sum_5 = 10
    expected_output_5 = False
    root_5 = create_tree_from_list(test_input_5)
    result_5 = hasPathSum(root_5, target_sum_5)
    print(f"Test 5: Input: {test_input_5}, Target Sum: {target_sum_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {result_5 == expected_output_5}")
    print()
    
    # Test case 6: Complex tree with multiple paths
    test_input_6 = [1,2,3,4,5,6,7]
    target_sum_6 = 7
    expected_output_6 = True  # Path: 1 -> 2 -> 4
    root_6 = create_tree_from_list(test_input_6)
    result_6 = hasPathSum(root_6, target_sum_6)
    print(f"Test 6: Input: {test_input_6}, Target Sum: {target_sum_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {result_6 == expected_output_6}")
    print()
    
    print("All test cases completed!") 