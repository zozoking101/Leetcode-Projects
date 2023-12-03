class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]  # Assume the first string as the initial prefix

        for string in strs[1:]:
        # Keep reducing the prefix until it is no longer a prefix of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
strs = ['elephant', 'elegant', 'element']
solution = Solution()
print(solution.longestCommonPrefix(strs))
    