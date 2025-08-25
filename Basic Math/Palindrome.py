def isPalindrome(self, n):
        rev=0
        org=n
        while(n>0):
            rem=n%10
            rev=(rev*10)+rem
            n=n//10
        return(rev==org)

# Input: n = 121
# Output: true
# Explanation: When read from left to right : 121.
# When read from right to left : 121.
