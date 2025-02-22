# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution(object):

    def longestCommonPrefix(self, strs):

        longest_prefix = ''
        smallest_word = min(strs, key=len)

        for index, char in enumerate(smallest_word):
            for i, word in enumerate(strs):

                if word[index] == char:
                    if i + 1 == len(strs):
                        longest_prefix += char 

                else:
                    return longest_prefix
                   

        return longest_prefix            


s = Solution()
strs = ["flow","flower", "fligth"]
print(s.longestCommonPrefix(strs))



# class Solution(object):
#     def longestPrefix(self, strs):

#         longest_prefix = ""
#         current_prefix = ''

#         for indice, word in enumerate(strs):
            
#             for other_word in strs[indice+1::]:

#                 if len(current_sufix) > len(longest_sufix):
#                     longest_prefix = current_prefix
#                     current_prefix = ''
#                     break

#                 for char1, char2 in zip(word, other_word):
#                     if char1 == char2:
#                         current_prefix += char1
                    
#                     else:
#                         break

#         return longest_prefix
    