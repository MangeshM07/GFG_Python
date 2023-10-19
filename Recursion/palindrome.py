def isStringPalindrome( input_string, start, end):
    if start >= end:
         return True
    return (input_string[start] == input_string[end] and isStringPalindrome(input_string, start+1, end-1))


input_string = 'malayalam'
print(isStringPalindrome(input_string, 0, len(input_string)-1))