#Write a program to evaluate the polynomial shown here: 3x3 - 5x2 + 6 for x = 2.55.

                 	  
degree = int(input("enter the number"))
coef=[]

for n in range(degree+1):
    coef.append(float(input(f"enter coefficeint for x ^{n}:")))

def solvepoly(a, b):
    result =0
    for i in range(len(a)):
        result += a[i]*(b**i)
    return result

remeber  =float(input("enter the value for x")) 
answer=solvepoly(coef,remeber)
print("the solution for the polynomial is "+str(answer))
