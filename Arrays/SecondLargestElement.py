"""
📘 Problem: Second Largest Element in an Array

Given an array of integers, find the second largest element.

---

🔹 Examples
Input: nums = [2, 4, 1, 7, 7]
Output: 4

Input: nums = [10, 10, 10]
Output: None

Input: nums = [-1, -2, -3, -4]
Output: -2

---

🔹 Constraints
- 1 ≤ n ≤ 10^5 (size of array)
- -10^9 ≤ nums[i] ≤ 10^9

---

🔹 Approaches

1️⃣ Brute Force (Sorting + Set)
- Remove duplicates using set
- Sort in descending order
- Second element is second largest
- Time Complexity: O(n log n)
- Space Complexity: O(n)

2️⃣ Optimized (Single Pass)
- Maintain two variables: largest and second largest
- Traverse once, update accordingly
- Time Complexity: O(n)
- Space Complexity: O(1)
"""

class Solution:
    # Brute Force Approach
    def secondLargestElementBruteForce(self, nums):
        nums = list(set(nums))        # remove duplicates
        nums.sort(reverse=True)       # sort descending
        if len(nums) < 2:
            return None               # no second largest
        return nums[1]

    # Optimized Approach
    def secondLargestElement(self, nums):
        maxele = float('-inf')
        seclar = float('-inf')

        for i in nums:
            if i > maxele:
                seclar = maxele
                maxele = i
            elif maxele > i > seclar:
                seclar = i

        return seclar if seclar != float('-inf') else None


# 🔹 Example Runs
if __name__ == "__main__":
    s = Solution()
    print(s.secondLargestElementBruteForce([2, 4, 1, 7, 7]))  # Output: 4
    print(s.secondLargestElement([2, 4, 1, 7, 7]))            # Output: 4
    print(s.secondLargestElement([10, 10, 10]))               # Output: None
    print(s.secondLargestElement([-1, -2, -3, -4]))           # Output: -2
