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
    # Define test cases as tuples: (name, p_tree, q_tree, expected)
    test_cases = [
        ("Basic example - identical trees", [1,2,3], [1,2,3], True),
        ("Different structure", [1,2], [1,None,2], False),
        ("Different values", [1,2,1], [1,1,2], False),
        ("Both trees are empty", [], [], True),
        ("One tree is empty, other is not", [], [1], False),
        ("Single node trees with same value", [5], [5], True),
        ("Single node trees with different values", [5], [3], False),
        ("Complex identical trees", [1,2,3,4,5,6,7], [1,2,3,4,5,6,7], True)
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, p_values, q_values, expected) in enumerate(test_cases, 1):
        p_root = create_tree_from_list(p_values)
        q_root = create_tree_from_list(q_values)
        result = isSameTree(p_root, q_root)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input p: {p_values}, Input q: {q_values}")
        print(f"Expected: {expected}, Got: {result}")
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