"""
Given the root of a binary tree, return an array of the largest value in each 
row of the tree (0-indexed).

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]
"""

from typing import List, Optional, Any
from collections import deque

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: Optional[TreeNode]) -> List[int]:
    """
    Find the largest value in each row of the binary tree.
    
    Intuition:
    Straight forward BFS approach. Comes down to five steps:
        1. define a row max value to negative infinity
        2. grab all the nodes on this level
        3. update row max as we iterate on row children
        4. add the children of each node to the queue
        5. append row max to the res list
    """
    if not root:
        return []
    queue = deque([root])
    res = []

    while queue:
        currMax = float("-inf")
        nodes_here: int = len(queue)
        for _ in range(nodes_here):
            curr = queue.popleft()
            currMax = max(currMax, curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(currMax)
    return res

def build_tree(values: List[Any]) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a list of values."""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
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
    test_input_1 = [1,3,2,5,3,None,9]
    expected_output_1 = [1,3,9]
    root_1 = build_tree(test_input_1)
    result_1 = largestValues(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [1,2,3]
    expected_output_2 = [1,3]
    root_2 = build_tree(test_input_2)
    result_2 = largestValues(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Single node
    test_input_3 = [5]
    expected_output_3 = [5]
    root_3 = build_tree(test_input_3)
    result_3 = largestValues(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Single node", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Left-skewed tree
    test_input_4 = [10,5,None,3,None,1]
    expected_output_4 = [10,5,3,1]
    root_4 = build_tree(test_input_4)
    result_4 = largestValues(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Left-skewed tree", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Right-skewed tree
    test_input_5 = [1,None,2,None,3,None,4]
    expected_output_5 = [1,2,3,4]
    root_5 = build_tree(test_input_5)
    result_5 = largestValues(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Right-skewed tree", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Complex tree with multiple levels
    test_input_6 = [10,5,15,3,7,12,18,1,4,6,8,11,13,16,20]
    expected_output_6 = [10,15,18,20]
    root_6 = build_tree(test_input_6)
    result_6 = largestValues(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Complex tree with multiple levels", passed_6))
    print(f"Test 6: Input: {test_input_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Tree with negative values
    test_input_7 = [-10,-5,-15,-3,-7,-12,-18]
    expected_output_7 = [-10,-5,-3]
    root_7 = build_tree(test_input_7)
    result_7 = largestValues(root_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Tree with negative values", passed_7))
    print(f"Test 7: Input: {test_input_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Tree with mixed positive and negative values
    test_input_8 = [5,-3,8,1,-7,6,9]
    expected_output_8 = [5,8,9]
    root_8 = build_tree(test_input_8)
    result_8 = largestValues(root_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Tree with mixed positive and negative values", passed_8))
    print(f"Test 8: Input: {test_input_8}")
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