"""
📘 Problem: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. 

Return the number of unique elements in nums.

---

🔹 Examples
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

---

🔹 Constraints
- 1 ≤ len(nums) ≤ 10^5
- -10^4 ≤ nums[i] ≤ 10^4
- nums is sorted in non-decreasing order

---

🔹 Approaches

1️⃣ Brute Force
- Use a set to store unique elements
- Convert back to list and overwrite original array
- Time Complexity: O(n log n) (due to set + sorting)
- Space Complexity: O(n)

2️⃣ Optimized (Two Pointers)
- Maintain index `i` for the last unique element
- Traverse with `j`, whenever nums[j] != nums[i], increment i and update
- Return i+1 as the length of unique elements
- Time Complexity: O(n)
- Space Complexity: O(1)
"""


class Solution:
    # Brute Force Approach
    def removeDuplicatesBruteForce(self, nums: List[int]) -> int:
        unique = sorted(set(nums))  # O(n log n)
        for i in range(len(unique)):
            nums[i] = unique[i]
        return len(unique)

    # Optimized Approach (Two Pointers)
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


# 🔹 Example Runs
if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 1, 2]
    k1 = s.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # Output: 2, [1,2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = s.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # Output: 5, [0,1,2,3,4]
