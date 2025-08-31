class Solution:
    # Brute Force Approach
    def largestElementBruteForce(self, nums):
        for i in nums:
            isLargest = True
            for j in nums:
                if j > i:
                    isLargest = False
                    break
            if isLargest:
                return i

    # Optimized Approach
    def largestElement(self, nums):
        maxele = nums[0]
        for i in nums:
            if i > maxele:
                maxele = i
        return maxele
# ️Brute Force
# Compare each element with all others.
# If no element is greater, that’s the largest.
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ️Optimized (Single Pass)
# Traverse array once while maintaining a variable maxele.
# Update maxele whenever a larger element is found.
# Time Complexity: O(n)
# Space Complexity: O(1)
