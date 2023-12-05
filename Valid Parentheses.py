class Solution(object):
    def isValid(self, s):
        open_brackets = '([{'
        close_brackets = ')]}'
        stack = []
        
        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif c in close_brackets:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if open_brackets.index(opening_bracket) != close_brackets.index(c):
                    return False
        
        return not stack
    
"""
In this solution, instead of directly comparing characters
with the stack's top element, we use the open_brackets
and close_brackets strings to determine the corresponding 
opening and closing brackets at the same index. This 
eliminates the need for multiple comparisons and simplifies
the code slightly.
"""

solution = Solution()
print(solution.isValid("([{(}])"))