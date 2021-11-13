# Method1
txt = str(10022001)

rev_txt = str(txt[::-1])

if txt == rev_txt:
    print("Given input is palindrome")
else:
    print("Not a palindrome")

# Method2

input_text = "ABCBA"
start_pos = 0
end_pos = len(input_text)-1

while start_pos < end_pos:
    if input_text[start_pos] != input_text[end_pos]:
        print("Not a palindrome")
        break
    else:
        start_pos += 1
        end_pos -= 1
else:
    print("palindrome")


