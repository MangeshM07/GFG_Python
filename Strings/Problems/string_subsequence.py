def check_string_subsequence(s1,s2):
    length = len(s2)
    prev_pos=0
    i,j = 0,0

    if len(s1) < len(s2):
        return False
    else:
        while (i < len(s1) and j < len(s2)):
            if s1[i] == s2[j]:
                j += 1
            i += 1
        if j == len(s2):
            return True
        else:
            return False


if __name__ == "__main__":
    str = "ABCD"
    search = "ADE"

    print(check_string_subsequence(str, search))