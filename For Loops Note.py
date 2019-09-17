Notes on For Loops in python

# Syntax of a for loop
my_iterable = [1,2,3]
for item_name in my_iterable:
  print(item_name)
  
>>1
>>2
>>3

Iterating through a list

# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
1
2
3
4
5
6
7
8
9
10
list_sum = 0

for num in list1:
    list_sum = list_sum + num

    print(list_sum)
1
3
6
10
15
21
28
36
45
55
for letter in 'Hell World':
    print(letter)
H
e
l
l
 
W
o
r
l
d
Great! Hopefully this makes sense. Now let's add an if statement to check for even numbers. We'll first introduce a new concept here--the modulo.

Modulo
The modulo allows us to get the remainder in a division and uses the % symbol. For example:

for num in list1:
    #Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')
Odd Number: 1
2
Odd Number: 3
4
Odd Number: 5
6
Odd Number: 7
8
Odd Number: 9
10
tup = (1,2,3)

for item in tup:
    print(item)
1
2
3
mylist = [(1,2), (3,4), (5,6), (7,8)]
len(mylist)
4
# Tuple Unpacking:
for (a,b) in mylist:
    print(b)
2
4
6
8
mylist2 = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist2:
    print(b)
2
6
9
