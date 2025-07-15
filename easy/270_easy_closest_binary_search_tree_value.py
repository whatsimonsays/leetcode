"""
Given the root of a binary search tree and a target value, return the value in 
the BST that is closest to the target. If there are multiple answers, print the smallest.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^9
- -10^9 <= target <= 10^9

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
"""

from typing import Optional, Any

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root: Optional[TreeNode], target: float) -> int:
    """
    Find the value in the BST that is closest to the target.
    
    Intuition:
    call a recursive function while keeping track of the absolute minimum
    difference between two values. 
    """
    if not root:
        raise ValueError("Cannot find closest value in empty tree")
    
    closest = root.val
    while root:
        closest = min(root.val, closest, key=lambda x: (abs(target-x), x))
        root = root.left if target < root.val else root.right
    return closest



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
    test_input_1 = [4,2,5,1,3]
    target_1 = 3.714286
    expected_output_1 = 4
    root_1 = build_tree(test_input_1)
    result_1 = closestValue(root_1, target_1)
    passed_1 = result_1 == expected_output_1
    test_results.append(("Test 1: Example 1", passed_1))
    print(f"Test 1: Input: {test_input_1}, target={target_1}")
    print(f"Expected: {expected_output_1}, Got: {result_1}")
    print(f"Pass: {passed_1}")
    print()
    
    # Test case 2: Example 2 from problem
    test_input_2 = [1]
    target_2 = 4.428571
    expected_output_2 = 1
    root_2 = build_tree(test_input_2)
    result_2 = closestValue(root_2, target_2)
    passed_2 = result_2 == expected_output_2
    test_results.append(("Test 2: Example 2", passed_2))
    print(f"Test 2: Input: {test_input_2}, target={target_2}")
    print(f"Expected: {expected_output_2}, Got: {result_2}")
    print(f"Pass: {passed_2}")
    print()
    
    # Test case 3: Target exactly matches a node value
    test_input_3 = [10,5,15,3,7,12,18]
    target_3 = 7.0
    expected_output_3 = 7
    root_3 = build_tree(test_input_3)
    result_3 = closestValue(root_3, target_3)
    passed_3 = result_3 == expected_output_3
    test_results.append(("Test 3: Target exactly matches a node value", passed_3))
    print(f"Test 3: Input: {test_input_3}, target={target_3}")
    print(f"Expected: {expected_output_3}, Got: {result_3}")
    print(f"Pass: {passed_3}")
    print()
    
    # Test case 4: Target between two values (choose smaller)
    test_input_4 = [10,5,15]
    target_4 = 7.5
    expected_output_4 = 5  # 5 is closer than 10 (distance 2.5 vs 2.5, choose smaller)
    root_4 = build_tree(test_input_4)
    result_4 = closestValue(root_4, target_4)
    passed_4 = result_4 == expected_output_4
    test_results.append(("Test 4: Target between two values", passed_4))
    print(f"Test 4: Input: {test_input_4}, target={target_4}")
    print(f"Expected: {expected_output_4}, Got: {result_4}")
    print(f"Pass: {passed_4}")
    print()
    
    # Test case 5: Target much larger than all values
    test_input_5 = [10,5,15,3,7,12,18]
    target_5 = 100.0
    expected_output_5 = 18
    root_5 = build_tree(test_input_5)
    result_5 = closestValue(root_5, target_5)
    passed_5 = result_5 == expected_output_5
    test_results.append(("Test 5: Target much larger than all values", passed_5))
    print(f"Test 5: Input: {test_input_5}, target={target_5}")
    print(f"Expected: {expected_output_5}, Got: {result_5}")
    print(f"Pass: {passed_5}")
    print()
    
    # Test case 6: Target much smaller than all values
    test_input_6 = [10,5,15,3,7,12,18]
    target_6 = -100.0
    expected_output_6 = 3
    root_6 = build_tree(test_input_6)
    result_6 = closestValue(root_6, target_6)
    passed_6 = result_6 == expected_output_6
    test_results.append(("Test 6: Target much smaller than all values", passed_6))
    print(f"Test 6: Input: {test_input_6}, target={target_6}")
    print(f"Expected: {expected_output_6}, Got: {result_6}")
    print(f"Pass: {passed_6}")
    print()
    
    # Test case 7: Target very close to a value
    test_input_7 = [10,5,15,3,7,12,18]
    target_7 = 6.999
    expected_output_7 = 7
    root_7 = build_tree(test_input_7)
    result_7 = closestValue(root_7, target_7)
    passed_7 = result_7 == expected_output_7
    test_results.append(("Test 7: Target very close to a value", passed_7))
    print(f"Test 7: Input: {test_input_7}, target={target_7}")
    print(f"Expected: {expected_output_7}, Got: {result_7}")
    print(f"Pass: {passed_7}")
    print()
    
    # Test case 8: Target exactly halfway between two values
    test_input_8 = [10,5,15]
    target_8 = 7.5
    expected_output_8 = 5  # Both 5 and 10 are 2.5 away, choose smaller
    root_8 = build_tree(test_input_8)
    result_8 = closestValue(root_8, target_8)
    passed_8 = result_8 == expected_output_8
    test_results.append(("Test 8: Target exactly halfway between two values", passed_8))
    print(f"Test 8: Input: {test_input_8}, target={target_8}")
    print(f"Expected: {expected_output_8}, Got: {result_8}")
    print(f"Pass: {passed_8}")
    print()
    
    # Test case 9: Single node with target close
    test_input_9 = [5]
    target_9 = 5.1
    expected_output_9 = 5
    root_9 = build_tree(test_input_9)
    result_9 = closestValue(root_9, target_9)
    passed_9 = result_9 == expected_output_9
    test_results.append(("Test 9: Single node with target close", passed_9))
    print(f"Test 9: Input: {test_input_9}, target={target_9}")
    print(f"Expected: {expected_output_9}, Got: {result_9}")
    print(f"Pass: {passed_9}")
    print()
    
    # Test case 10: Large BST with precise target
    test_input_10 = [50,25,75,12,37,62,87,6,18,31,43,56,68,81,93]
    target_10 = 35.7
    expected_output_10 = 37  # 37 is closest to 35.7
    root_10 = build_tree(test_input_10)
    result_10 = closestValue(root_10, target_10)
    passed_10 = result_10 == expected_output_10
    test_results.append(("Test 10: Large BST with precise target", passed_10))
    print(f"Test 10: Input: {test_input_10}, target={target_10}")
    print(f"Expected: {expected_output_10}, Got: {result_10}")
    print(f"Pass: {passed_10}")
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