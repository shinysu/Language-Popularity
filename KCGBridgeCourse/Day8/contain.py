"""
function to check if substring is in the string or not
"""

def contains_substring(s, sub):
    if sub in s:
        return True
    else:
        return False


s = input("Enter the string: ")
sub = input("Enter the substring to find: ")
print(contains_substring(s, sub))

