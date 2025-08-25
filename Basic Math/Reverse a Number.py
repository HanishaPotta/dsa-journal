# Problem: Count Digits
# Source: Striver DSA Sheet
# Difficulty: Easy

def reverseNumber(self, n):
        rev=0
        while(n>0):
            rem=n%10
            rev=(rev*10)+rem
            n=n//10
        return(rev)
  
# Example:
# Input: n = 123
# Output: 321
# Explanation: Reverse of 123 is 321.
