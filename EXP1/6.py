#Write a program to count occurrences of all characters within a string
input_string = input("Enter the String")
char_count={}
for char in input_string:
    char_count[char]=char_count.get(char,0)+1

for char,count in char_count.items():
    print(f"char is:{char} and its count is {count}")