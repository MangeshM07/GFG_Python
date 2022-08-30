def pattern_search(s, pattern):
    pos = s.find(pattern)

    while pos >= 0:
        print(pos)
        pos = s.find(pattern, pos+1)


if __name__ == "__main__":
    s1 = "geeks for geeks"
    pattern = "geeks"
    pattern_search(s1, pattern)

    s2 = "AAAAA"
    pattern = "AAA"
    pattern_search(s2, pattern)


