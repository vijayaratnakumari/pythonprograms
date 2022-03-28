'''n =int (input("enter number:"))
s = 0

for i in range(1, n+1):
    s = s+i
print("sum of ", n, "numbers:", s)'''

#bitwise operators
'''a=10
b=12
print(bin(a))
print(bin(b))
print(bin(a&b))
print(bin(a|b))
print(bin(a^b))
print(bin(~a))
print(bin(~b))'''

#if, if else, else if

'''i = 10

if i ==100:
    print("true")
else:
    print("false")

j =int(input("enter number1:"))
k =int(input("enter numnber2:"))
if j>k:
    print(j, "is big ")
else:
    print(k, "is big")
#ternary operator

i= int(input("enter number1:"))
j= int(input("enter number2:"))
k=int(input("enter number3:"))
max =i if i>j and i>k else j if j>k else k
print("max value is:", max)'''

#else if, nested if, elif

i =int(input("enter number:"))
if i>20:
    print(i, "is greater than 20:")
else:
    if i>15:
        print(i, "is greater than 15:")
    else:
        print(i, "is not greater than 15 and 20")
