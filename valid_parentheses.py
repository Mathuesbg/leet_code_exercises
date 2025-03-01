# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:

    def isValid(self, s: str) -> bool:

        temp = []

        for char in s:
            if char in "{[(":
                temp.append(char)
            
            elif len(temp) > 0:
                    
                    last_char = temp[-1]

                    if last_char == "{" and char == "}" or last_char == "[" and char == "]" or last_char == "(" and char == ")":
                        temp.pop()
                    
                    else:        
                        return False    
            else:
                return False
            
        return len(temp) == 0


        
f = Solution()
print(f.isValid(s= "(){[{[]}]}[]"))