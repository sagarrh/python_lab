# Replace each special symbol with # in the following string: 

# I/p string:Mary @always &stood firl̥st in %class 

# O/P String: Mary #always #stood first in #class 

inputstring=input("enter")
specialsym ="!@#$%^&*()_+-={|?><,/*-./}"
for char in specialsym:
    inputstring=inputstring.replace(char,'#')
    
print(inputstring)