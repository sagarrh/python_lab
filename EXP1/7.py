# Write a program to find the last position of a substring “Rama” in a given string  

#                For e.g. "Mary always stood first in class. Mary now works at Google." 

#                The expected outcome is “The last position of Mary starts at index 34” 

input_string = input("enter")
substring=input("substring")
lastcount = input_string.rfind(substring)
print(lastcount)

