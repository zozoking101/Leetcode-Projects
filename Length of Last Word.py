class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return(len(s.split()[-1]))
solution = Solution()
print(solution.lengthOfLastWord('fly    me   to the       moon'))