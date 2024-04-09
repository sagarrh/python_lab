# Write a Python program to count the elements in a list until an element is a tuple

sagar_list=[2,3,4,5,2,(2,3,4),2,4,0]
count=0
for item in sagar_list:
    if isinstance(item,tuple):
        break
    count+=1
print(f"count is equal to {count}")