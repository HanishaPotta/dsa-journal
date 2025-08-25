# Problem: Count Digits
# Source: Striver DSA Sheet
# Difficulty: Easy

def countDigit(self, n):
        count=0
        while(n>0):
            lastdig=n%10
            n=n//10
            count+=1
        return(count)

# Example:
# Input: n = 14
# Output: 2
# Explanation: There are 2 digits in 14.
