# # Given a string s, find the length of the longest substring without repeating characters.

# def lengthOfLongestSubstring(s: str) -> int:
#     start = 0
#     en_uzun = 0
#     dictim = {}
#     for i in range(len(s)):
#         if i in dictim :
#             dictim[s[i]] = i
#     return en_uzun

# # res = ""
# #     liste = []
# #     dicte = {}
# #     for i in s:
# #         if i not in dicte:
# #             dicte[i] = 1
# #             res += i
# #         else:
# #             dict.clear()
# #             liste.append(res)
# #             res = ""
# #     return liste

# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("pwwkew"))    