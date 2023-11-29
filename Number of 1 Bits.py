class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        try:
            count_one = n.count('1')
            return count_one
        except Exception:
            print("Invalid input")
        
# Solution instance
solution = Solution()
binary_string = '00000000000000000000000000001011'
print(solution.hammingWeight(binary_string))