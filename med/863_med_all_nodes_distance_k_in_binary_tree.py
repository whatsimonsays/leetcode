"""
Given the root of a binary tree, the value of a target node target, and an 
integer k, return an array of the values of all nodes that have a distance k 
from the target node.

You can return the answer in any order.

Constraints:
- The number of nodes in the tree is in the range [1, 500].
- 0 <= Node.val <= 500
- All the values Node.val are unique.
- target is the value of one of the nodes in the tree.
- 0 <= k <= 1000

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 
5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []
"""

from typing import List, Optional
from collections import defaultdict, deque

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None

def distanceK(root: Optional[TreeNode], target: Optional[TreeNode], k: int) -> List[int]:
    """
    Find all nodes at distance k from the target node.
    
    Intuition:
    1. can create the equivalency matrix or just add parent pointers to each node.
    Ill just default to the parent pointers.
    2. run dfs on each level starting at the target node.
    3. set a distance to 0 < k and the final queue with the children are the paths
    """
    if not root or not target:
        return []

    def dfs(node, parent):
        if node:
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root, None)

    seen = set()
    seen.add(target)
    queue = deque([target])
    distance = 0
    while queue and distance < k:
        current_length = len(queue)
        for _ in range(current_length):
            node = queue.popleft()
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        distance += 1
    return [node.val for node in queue]

if __name__ == "__main__":
    # Helper function to create a tree from a list (for testing)
    def create_tree(values, index=0):
        if index >= len(values) or values[index] is None:
            return None
        root = TreeNode(values[index])
        root.left = create_tree(values, 2 * index + 1)
        root.right = create_tree(values, 2 * index + 2)
        return root
    
    # Helper function to find a node by value
    def find_node(root, target_val):
        if not root:
            return None
        if root.val == target_val:
            return root
        left = find_node(root.left, target_val)
        if left:
            return left
        return find_node(root.right, target_val)
    
    # Define test cases as tuples: (name, tree_values, target_val, k, expected)
    test_cases = [
        ("Example 1", [3,5,1,6,2,0,8,None,None,7,4], 5, 2, [7,4,1]),
        ("Example 2", [1], 1, 3, []),
        ("Single node k=0", [5], 5, 0, [5]),
        ("Single node k=1", [5], 5, 1, []),
        ("Two nodes k=1", [1,2], 1, 1, [2]),
        ("Two nodes k=0", [1,2], 1, 0, [1]),
        ("Three nodes linear", [1,2,3], 2, 1, [1]),
        ("Three nodes linear k=2", [1,2,3], 2, 2, [3]),
        ("Target is leaf", [1,2,3], 3, 1, [1]),
        ("Complex tree", [3,5,1,6,2,0,8,None,None,7,4], 5, 0, [5]),
        ("Complex tree k=1", [3,5,1,6,2,0,8,None,None,7,4], 5, 1, [6,2,3]),
        ("Complex tree k=3", [3,5,1,6,2,0,8,None,None,7,4], 5, 3, [0,8]),
        ("Target at root", [3,5,1,6,2,0,8,None,None,7,4], 3, 1, [5,1]),
        ("Target at root k=2", [3,5,1,6,2,0,8,None,None,7,4], 3, 2, [6,2,0,8]),
        ("Large k", [1,2,3,4,5,6,7], 4, 10, []),
        ("Balanced tree", [1,2,3,4,5,6,7], 2, 1, [1,4,5]),
        ("Balanced tree k=2", [1,2,3,4,5,6,7], 2, 2, [3]),
        ("Unbalanced tree", [1,2,None,3,None,None,None,4], 2, 1, [1,3]),
        ("Unbalanced tree k=2", [1,2,None,3,None,None,None,4], 2, 2, [4]),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, tree_values, target_val, k, expected) in enumerate(test_cases, 1):
        # Create the tree
        root = create_tree(tree_values)
        target = find_node(root, target_val)
        
        result = distanceK(root, target, k)
        # Sort both lists for comparison since order doesn't matter
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        passed = result_sorted == expected_sorted
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input: tree={tree_values}, target={target_val}, k={k}")
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