mysentence = (input("Enter a string : ")) # Input
str = "The quick brown fox jumps over the lazy dog." # initial string
reversed = "".join(reversed(str)) #.join() method merges all of the characters
print("Every second letter of your reversed string:", reversed[0:43:2]) # print the reversed string