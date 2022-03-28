#write a table by using for loop
num = int(input("enter number:"))

for i in range(1, 11):
    print(num,'x', i, '=', num*i)

# even and odd numbers
'''Enter the starting number of range 5
enter the ending number of range 15
orginal number list=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even number list= [6, 8, 10, 12, 14]
odd number list = [5, 7, 9, 11, 13, 15]

A = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
OddList = []
EvenList = []
for i in A:
    if (i%2) == 0:
        print(i,"is enven number:" )
    else:
        print(i, "is odd number:")
    EvenList.append(i)

else:
    OddList.append(i)
    print("even number", EvenList)
    print("Odd numbers", OddList)'''

#Example 1: Using while loop

# Python program to count Even and Odd numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

even_count, odd_count = 0, 0
num = 0

# using while loop
while (len(list1) > num):

    # checking condition
    if list1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # increment num
    num += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

#Example 2: Using for loop

# Python program to count Even
# and Odd numbers in a List

# list of numbers
'''list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)'''

#Example 3 : Using Python Lambda Expressions

# list of numbers
'''list1 = [10, 21, 4, 45, 66, 93, 11]

odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))

# we can also do len(list1) - odd_count
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)'''

#Example 4 : Using List Comprehension

# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

only_odd = [num for num in list1 if num % 2 == 1]
odd_count = len(only_odd)

print("Even numbers in the list: ", len(list1) - odd_count)
print("Odd numbers in the list: ", odd_count)
