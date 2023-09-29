# a string is palindrom or not 

def palindrome(text, start):
    end = len(text)-1-start
    if start >= end:
        return True
    if text[start] != text[end]:
        return False
    return palindrome(text, start+1)

text = "madam"
print(palindrome(text, 0))


















