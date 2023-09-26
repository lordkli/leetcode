# inp = "szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni"

inp = "aabbbccde"
# o 12
# m 11
# n 11

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
# b 3
# a 2
# c 2


# def fonk(inp):
#     d = {}
#     for i in inp:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1

#     sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse=True)

#     output = ""
#     for i in sorted_dict[0:2]:
#         output += str(i[0]) + " " + str(i[1]) +"\n"

#     output += str(sorted_dict[2][0]) + " " + str(sorted_dict[2][1])
#     return output


# print(fonk(input))

#! SOLUTION
if __name__ == "__main__":
    d = {}
    for i in inp:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    # print(d)  #{'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 1}

    # sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse=True)
    # ('a': 2), ('b': 3), (a,b)
    sorted_liste = sorted(d.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)

    print(sorted_liste)
    
    for i in sorted_liste[:3]:
        print(i[0], i[1])


#! SOLUTION
# from collections import Counter

# dict_list = sorted(
#     list(Counter(sorted(input)).items()), key=lambda x: x[1], reverse=True
# )
# for character, amount in dict_list[:3]:
#     print(character, amount)

#! SOLUTION
# from collections import Counter, OrderedDict


# class OrderedCounter(Counter, OrderedDict):
#     pass


# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]


# s = input()
# count = {}
# for val in s:
#     if count.get(val):
#         count[val] += 1
#     else:
#         count[val] = 1

# items = count.items()
# items = sorted(items, key=lambda x: (x[1], -ord(x[0])), reverse=True)
# for i in range(3):
#     print(items[i][0], items[i][1])



from collections import Counter, OrderedDict
