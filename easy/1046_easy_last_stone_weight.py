"""
You are given an array of integers stones where stones[i] is the weight of the 
ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two 
stones and smash them together. Suppose the heaviest two stones have weights x 
and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has 
new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, 
return 0.

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value 
of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Example 3:
Input: stones = [1,1]
Output: 0
Explanation: We combine 1 and 1 to get 0. The array converts to [0] then that's 
the value of the last stone.
"""

from typing import List
from heapq import heapify, heappop, heappush

def lastStoneWeight(stones: List[int]) -> int:
    """
    Find the weight of the last remaining stone after smashing the heaviest two 
    stones in each turn.
    
    Intuition:
    1. create a max heap
    2. pop two elements while length of max heap is greater than 1
    3. smash together
    4. insert winner to the heap
    5. return the last element
    """
    maxheap = [-stone for stone in stones]
    heapify(maxheap)

    while len(maxheap) > 1:
        a, b = -heappop(maxheap), -heappop(maxheap)
        if a != b:
            heappush(maxheap, -(a-b))
    
    return -maxheap[0] if maxheap else 0

if __name__ == "__main__":
    # Define test cases as tuples: (name, stones, expected)
    test_cases = [
        ("Example 1", [2,7,4,1,8,1], 1),
        ("Example 2", [1], 1),
        ("Example 3", [1,1], 0),
        ("Single stone", [5], 5),
        ("Two stones same weight", [3,3], 0),
        ("Two stones different weight", [3,5], 2),
        ("Three stones", [1,2,3], 0),
        ("Four stones", [1,2,3,4], 0),
        ("All same weight", [2,2,2,2], 0),
        ("All different weights", [1,3,5,7], 0),
        ("Large weights", [1000,500,250,125], 125),
        ("Small weights", [1,1,1,1,1], 1),
        ("Mixed weights", [10,5,15,20,25], 5),
        ("Repeated weights", [2,2,2,2,2,2,2,2], 0),
        ("One heavy stone", [1,1,1,1,1,1,1,1000], 993),
        ("Edge case max length", [1]*30, 0),
        ("Edge case min length", [1], 1),
        ("Edge case max weight", [1000], 1000),
        ("Edge case min weight", [1], 1),
        ("All destroyed", [2,2,2,2,2,2], 0),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, stones, expected) in enumerate(test_cases, 1):
        result = lastStoneWeight(stones)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Input stones: {stones}")
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