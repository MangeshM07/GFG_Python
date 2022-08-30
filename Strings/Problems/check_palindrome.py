def check_palindrome(str):
    if len(str) <= 1:
        return True
    else:
        starting_pos = 0
        ending_pos = len(str) - 1
        new_str = ""
        while starting_pos < ending_pos:
            if str[starting_pos] != str[ending_pos]:
                print("Not a palindrome")
                break
            starting_pos += 1
            ending_pos -= 1

        else:
            print("It is palindrome")

def check_palindrome1(str):
    new_str = str[::-1]
    if str == new_str:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")


if __name__ == "__main__":
    input = "MALAYALAM"
    check_palindrome(input)