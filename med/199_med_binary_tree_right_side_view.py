"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
"""

from typing import List, Optional
from collections import deque

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    """
    Return the values of nodes visible from the right side of the binary tree.
    
    Intuition:
    This one is pretty straight forward to me. We want to go BFS search because we will
    be going level by level. Basically three steps here...
        1. Grab all the nodes in the current level
        2. print the value of the last node on this level. (In our case just add to res)
        3. for each node on this level, append the children to the queue
    """
    if not root:
        return []
    
    res = []
    queue = deque([root])
    while queue:
        nodes_in_level = len(queue)
        # 1. Append last node in this level to the result list
        res.append(queue[-1].val)
        for _ in range(nodes_in_level):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return res
    


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
    test_input_1 = [1,2,3,None,5,None,4]
    expected_output_1 = [1,3,4]
    root_1 = create_tree_from_list(test_input_1)
    result_1 = rightSideView(root_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [1,None,3]
    expected_output_2 = [1,3]
    root_2 = create_tree_from_list(test_input_2)
    result_2 = rightSideView(root_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Empty tree
    test_input_3 = []
    expected_output_3 = []
    root_3 = create_tree_from_list(test_input_3)
    result_3 = rightSideView(root_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Empty tree", passed_3))
    print(f"Test 3: Input: {test_input_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Single node
    test_input_4 = [1]
    expected_output_4 = [1]
    root_4 = create_tree_from_list(test_input_4)
    result_4 = rightSideView(root_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Single node", passed_4))
    print(f"Test 4: Input: {test_input_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Left-skewed tree
    test_input_5 = [1,2,None,3,None,4]
    expected_output_5 = [1,2,3,4]
    root_5 = create_tree_from_list(test_input_5)
    result_5 = rightSideView(root_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Left-skewed tree", passed_5))
    print(f"Test 5: Input: {test_input_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Right-skewed tree
    test_input_6 = [1,None,2,None,3,None,4]
    expected_output_6 = [1,2,3,4]
    root_6 = create_tree_from_list(test_input_6)
    result_6 = rightSideView(root_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Right-skewed tree", passed_6))
    print(f"Test 6: Input: {test_input_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Balanced tree
    test_input_7 = [1,2,3,4,5,6,7]
    expected_output_7 = [1,3,7]
    root_7 = create_tree_from_list(test_input_7)
    result_7 = rightSideView(root_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Balanced tree", passed_7))
    print(f"Test 7: Input: {test_input_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Complex tree with missing right nodes
    test_input_8 = [1,2,3,4,5,None,None,6,7,None,None,None,None,8,9]
    expected_output_8 = [1,3,5,7,9]
    root_8 = create_tree_from_list(test_input_8)
    result_8 = rightSideView(root_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Complex tree", passed_8))
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