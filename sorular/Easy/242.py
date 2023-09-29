# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


from collections import Counter


s = "rat"
t = "car"

#! SOLUTION 1
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    dict_1 = {}
    dict_2 = {}

    for i in s:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1

    for i in t:
        if i in dict_2:
            dict_2[i] += 1
        else:
            dict_2[i] = 1

    print(dict_1)
    print(dict_2)

    return dict_1 == dict_2


print(isAnagram(s, t))

#! NOTE
# dicte siralar farkli olsada ayni ise ayniya ulasiyoruz
d = {"a": 3, "b": 2}
c = {"b": 2, "a": 3}

print(d == c)



#! SOLUTION
def isAnagram(s, t):
    return Counter(s) == Counter(t)