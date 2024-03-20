# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


from ast import List


def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""

    res = strs[0]
    
    while len(res) > 0:
        for i in strs:
            if res not in i:
                res = res[0:-1]
            else:
                return res
    return ""

input  = ["flower","flow","flight"]

print(longestCommonPrefix(input))