from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater = {}
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(n, -1) for n in nums1]


if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    output =  [-1,3,-1]

    assert(nextGreaterElement(nums1, nums2) == output)