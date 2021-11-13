def check_anagram(s1,s2):
    if len(s1) == len(s2):
        return False

    count = [0]*256

    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1

    for x in count:
        if x != 0:
            return False
    return True


# s1 = "listen"
# s2 = "silent"
# check_anagram(s1, s2)
#
# s1 = "aacb"
# s2 = "acab"
# check_anagram(s1, s2)

s1 = "aab"
s2 = "abb"


if check_anagram(s1, s2):
    print("Given strings are anagram")
else:
    print("Given strings are not anagram")


