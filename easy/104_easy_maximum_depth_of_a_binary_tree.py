# Definition for a binary tree node.
import pytest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def test_maxDepth_empty():
    assert maxDepth(None) == 0

def test_maxDepth_single_node():
    root = TreeNode(1)
    assert maxDepth(root) == 1

def test_maxDepth_left_skewed():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert maxDepth(root) == 3

def test_maxDepth_right_skewed():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert maxDepth(root) == 3

def test_maxDepth_balanced():
    #      1
    #     / \
    #    2   3
    #   /   / \
    #  4   5   6
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4)),
                    TreeNode(3, TreeNode(5), TreeNode(6)))
    assert maxDepth(root) == 3

def test_maxDepth_unbalanced():
    #      1
    #     /
    #    2
    #   /
    #  3
    #   \
    #    4
    root = TreeNode(1, TreeNode(2, TreeNode(3, None, TreeNode(4))))
    assert maxDepth(root) == 4
    
if __name__ == "__main__":
    # Sample test cases
    print("Testing maxDepth function with various tree structures:")
    
    # Test 1: Empty tree
    print(f"Empty tree depth: {maxDepth(None)}")  # Expected: 0
    
    # Test 2: Single node
    root1 = TreeNode(1)
    print(f"Single node depth: {maxDepth(root1)}")  # Expected: 1
    
    # Test 3: Simple left-skewed tree
    #     1
    #    /
    #   2
    #  /
    # 3
    root2 = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(f"Left-skewed tree depth: {maxDepth(root2)}")  # Expected: 3
    
    # Test 4: Simple right-skewed tree
    #   1
    #    \
    #     2
    #      \
    #       3
    root3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(f"Right-skewed tree depth: {maxDepth(root3)}")  # Expected: 3
    
    # Test 5: Balanced tree
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   5   6
    root4 = TreeNode(1,
                     TreeNode(2, TreeNode(4)),
                     TreeNode(3, TreeNode(5), TreeNode(6)))
    print(f"Balanced tree depth: {maxDepth(root4)}")  # Expected: 3
    
    # Test 6: Complex unbalanced tree
    #       1
    #      /
    #     2
    #    /
    #   3
    #    \
    #     4
    root5 = TreeNode(1, TreeNode(2, TreeNode(3, None, TreeNode(4))))
    print(f"Complex unbalanced tree depth: {maxDepth(root5)}")  # Expected: 4
    
    print("\nAll sample tests completed!")
