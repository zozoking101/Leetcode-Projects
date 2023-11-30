class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return(s == s[::-1]) 
solution = Solution()
x = 121
print(solution.isPalindrome(x))