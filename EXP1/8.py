# Removal all characters from a string except integers 
in_string=input("enter")

str1 = ''.join(filter(str.isdigit,in_string))
print(str1)