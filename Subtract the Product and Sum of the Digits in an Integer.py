class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        j=0
        for s in str(n):
            i *= int(s)
            j += int(s)
        return(i-j)
solution = Solution()
print(solution.subtractProductAndSum('4421'))