# idea here is to store the string in the varibale and 
# look for the next element and if next element is present in the string
#  then we slice the original string and we add the repeated string to the
#  original value and see the max length function for the longest
#  substring 

def longest_substring(string_):
    lon_str = ""
    max_ = 0
    for char in string_:
        if char not in lon_str:
            lon_str += char
        else:
            lon_str = lon_str[lon_str.index(char)+1:] + char
        max_ = max(max_,len(lon_str)) 
    return max_

print(longest_substring('abcabcbb'))