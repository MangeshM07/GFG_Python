def reverse_sentence(s):
    s1 = s.split()
    new_str = s1[::-1]
    s2=""
    for i in range(len(new_str)):
        s2 += new_str[i]+" "

    return s2.strip()


if __name__ == "__main__":
    s = "welcome to gfg"
    print(reverse_sentence(s))

    s = "I Love Coding"
    print(reverse_sentence(s))

    s = "abc"
    print(reverse_sentence(s))