#Arrange string characters such that lowercase letters should come first.  For example: str1=’PyTHon” then output should be “yonPTH” 
str = input("enter the string")

lower= ''.join([char for char in str if char.islower()])
upper= ''.join([char for char in str if char.isupper()])

final = lower+upper
print(final)