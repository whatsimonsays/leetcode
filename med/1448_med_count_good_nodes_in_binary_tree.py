"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path starting from the root.
Node 3 -> (3,1,3) is the maximum value in the path starting from the root.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""

from typing import Optional

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: Optional[TreeNode]) -> int:
    """
    Count the number of good nodes in a binary tree.
    A node is considered good if it has the maximum value in the path from root to that node.
    
    Intuition:

    """
    if root is None:
        return 0

    def dfs(root, localMaximum) -> int:
        curr = 1 if root.val >= localMaximum else 0
        localMaximum = max(root.val, localMaximum)
        left = dfs(root.left, localMaximum) if root.left else 0
        right = dfs(root.right, localMaximum) if root.right else 0

        return left + right + curr

    return dfs(root, root.val)

def create_tree_from_list(values: list) -> Optional[TreeNode]:
    """
    Helper function to create a binary tree from a list representation.
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
    # Test case 1: Basic example
    test_input_1 = [3,1,4,3,None,1,5]
    expected_output_1 = 4
    root_1 = create_tree_from_list(test_input_1)
    result_1 = goodNodes(root_1)
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {result_1 == expected_output_1}")
    print()
    
    # Test case 2: Another example
    test_input_2 = [3,3,None,4,2]
    expected_output_2 = 3
    root_2 = create_tree_from_list(test_input_2)
    result_2 = goodNodes(root_2)
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {result_2 == expected_output_2}")
    print()
    
    # Test case 3: Single node
    test_input_3 = [1]
    expected_output_3 = 1
    root_3 = create_tree_from_list(test_input_3)
    result_3 = goodNodes(root_3)
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {result_3 == expected_output_3}")
    print()
    
    # Test case 4: All nodes are good (increasing values)
    test_input_4 = [1,2,3,4,5]
    expected_output_4 = 5
    root_4 = create_tree_from_list(test_input_4)
    result_4 = goodNodes(root_4)
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {result_4 == expected_output_4}")
    print()
    
    # Test case 5: Only root is good (decreasing values)
    test_input_5 = [5,4,3,2,1]
    expected_output_5 = 1
    root_5 = create_tree_from_list(test_input_5)
    result_5 = goodNodes(root_5)
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {result_5 == expected_output_5}")
    print()
    
    print("All test cases completed!") 