"""
Given the root of a binary tree, invert the tree, and return its root.

To invert a binary tree, swap every left node with its corresponding right node.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Explanation: The tree has been inverted.

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
Explanation: The tree has been inverted.

Example 3:
Input: root = []
Output: []
Explanation: An empty tree is returned.
"""

from typing import Optional, List
from collections import deque

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert a binary tree by swapping every left node with its corresponding right node.
    
    Intuition:
    just go level by level using BFS and swap left with right
    """
    if not root:
        return root
    
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    
    return root


# Helper function to create a binary tree from a list
def buildTree(values: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    """Build a binary tree from a list representation."""
    if index >= len(values) or values[index] is None:
        return None
    
    val = values[index]
    root = TreeNode(val if val is not None else 0)
    root.left = buildTree(values, 2 * index + 1)
    root.right = buildTree(values, 2 * index + 2)
    return root

# Helper function to convert a binary tree to a list
def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Convert a binary tree to a list representation."""
    if not root:
        return []
    
    result = []
    queue: List[Optional[TreeNode]] = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

if __name__ == "__main__":
    # Define test cases as tuples: (name, input_tree, expected_output)
    test_cases = [
        ("Example 1", [4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ("Example 2", [2,1,3], [2,3,1]),
        ("Example 3", [], []),
        ("Single node", [1], [1]),
        ("Two nodes left", [1,2], [1,None,2]),
        ("Two nodes right", [1,None,2], [1,2]),
        ("Three nodes", [1,2,3], [1,3,2]),
        ("Four nodes", [1,2,3,4], [1,3,2,None,None,None,4]),
        ("Five nodes", [1,2,3,4,5], [1,3,2,None,None,5,4]),
        ("Seven nodes", [1,2,3,4,5,6,7], [1,3,2,7,6,5,4]),
        ("Right skewed", [1,None,2,None,None,None,3], [1,2,None,3]),
        ("Complete tree", [1,2,3,4,5,6,7], [1,3,2,7,6,5,4]),
        ("Unbalanced", [1,2,3,4,None,None,7], [1,3,2,7,None,None,4]),
        ("Deep tree", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,3,2,7,6,5,4,15,14,13,12,11,10,9,8]),
        ("Negative values", [-1,-2,-3], [-1,-3,-2]),
        ("Large values", [100,50,150,25,75,125,175], [100,150,50,175,125,75,25]),
        ("Zero values", [0,1,2], [0,2,1]),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, input_tree, expected_output) in enumerate(test_cases, 1):
        # Build the input tree
        root = buildTree(input_tree)
        
        # Invert the tree
        inverted_root = invertTree(root)
        
        # Convert back to list
        result = treeToList(inverted_root)
        
        # Check if results match
        passed = result == expected_output
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input tree: {input_tree}")
        print(f"Expected: {expected_output}")
        print(f"Got: {result}")
        print(f"Pass: {passed}")
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