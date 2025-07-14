"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4].
- 1 <= Node.val <= 10^5
- 1 <= low <= high <= 10^5
- All Node.val are unique.

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""

from typing import Optional, Any

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    
    res = 0
    if low <= root.val <= high:
        res += root.val
    
    if root.val > low:
        res += rangeSumBST(root.left, low, high)
    
    if root.val < high:
        res += rangeSumBST(root.right, low, high)
    
    return res

def build_tree(values: list) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a list of values."""
    if not values or values[0] is None:
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
    test_input_1 = [10,5,15,3,7,None,18]
    low_1, high_1 = 7, 15
    expected_output_1 = 32
    root_1 = build_tree(test_input_1)
    result_1 = rangeSumBST(root_1, low_1, high_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}, low={low_1}, high={high_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [10,5,15,3,7,13,18,1,None,6]
    low_2, high_2 = 6, 10
    expected_output_2 = 23
    root_2 = build_tree(test_input_2)
    result_2 = rangeSumBST(root_2, low_2, high_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}, low={low_2}, high={high_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Single node in range
    test_input_3 = [5]
    low_3, high_3 = 3, 7
    expected_output_3 = 5
    root_3 = build_tree(test_input_3)
    result_3 = rangeSumBST(root_3, low_3, high_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Single node in range", passed_3))
    print(f"Test 3: Input: {test_input_3}, low={low_3}, high={high_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Single node not in range
    test_input_4 = [5]
    low_4, high_4 = 10, 15
    expected_output_4 = 0
    root_4 = build_tree(test_input_4)
    result_4 = rangeSumBST(root_4, low_4, high_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Single node not in range", passed_4))
    print(f"Test 4: Input: {test_input_4}, low={low_4}, high={high_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: All nodes in range
    test_input_5 = [10,5,15,3,7,13,18]
    low_5, high_5 = 1, 20
    expected_output_5 = 71  # 3+5+7+10+13+15+18 = 71
    root_5 = build_tree(test_input_5)
    result_5 = rangeSumBST(root_5, low_5, high_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: All nodes in range", passed_5))
    print(f"Test 5: Input: {test_input_5}, low={low_5}, high={high_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: No nodes in range
    test_input_6 = [10,5,15,3,7,13,18]
    low_6, high_6 = 20, 25
    expected_output_6 = 0
    root_6 = build_tree(test_input_6)
    result_6 = rangeSumBST(root_6, low_6, high_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: No nodes in range", passed_6))
    print(f"Test 6: Input: {test_input_6}, low={low_6}, high={high_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Range includes only some nodes
    test_input_7 = [20,10,30,5,15,25,35]
    low_7, high_7 = 12, 28
    expected_output_7 = 60  # 15+20+25 = 60
    root_7 = build_tree(test_input_7)
    result_7 = rangeSumBST(root_7, low_7, high_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Range includes only some nodes", passed_7))
    print(f"Test 7: Input: {test_input_7}, low={low_7}, high={high_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Large BST with specific range
    test_input_8 = [50,25,75,12,37,62,87,6,18,31,43,56,68,81,93]
    low_8, high_8 = 30, 60
    expected_output_8 = 217  # 31+37+43+50+56 = 217
    root_8 = build_tree(test_input_8)
    result_8 = rangeSumBST(root_8, low_8, high_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Large BST with specific range", passed_8))
    print(f"Test 8: Input: {test_input_8}, low={low_8}, high={high_8}")
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