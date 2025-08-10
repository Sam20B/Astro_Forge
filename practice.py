#adding/removing items from a tuple by converting it into a list
#then back to a tuple
x = ("apple","avocado","mango")
z = list(x)
z.pop(2)
x = tuple(z)

print(x)

#unpacking a tuple
x = ("apple","avocado","mango","kiwi","orange")
a,*b,c = x
print(a)
print(b)
print(c)
k = x.index("mango")
print(k)

#dictionaries
mydict = {
    "year" : "2014",
    "year" : "1920",
    "car" : "outlander"
}
thisdict = mydict.copy()
mydict.pop("year")
print(mydict)
print(thisdict)

#multiple dictionaries in one dictionary
child1 = {
    "name" : "John",
    "age" : 10
}
child2 = {
    "name" : "Jane",
    "age" : 12
}
child3 = {
    "name" : "Jim",
    "age" : 9
}

parent = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(parent)
print(parent["child2"]["name"])

#if statements
a = 77
b = 83
if b > a:
    print("Yeah a got none on b lmao!")
else:
    print("a is greater mahn:(")

#checking if an item entered is on the list and adding it if it's not
'''x = ['avocado','cake','tissue','wipes']
a = str(input())
if a in x:
    print("already added")
else:
    print("adding " + a + " to list...")
    x.append(a)
print(x)'''

#match expression instead of if...else statements
target = "joy"
gender = "girl"
match target:
    case "chris"|"ian"|"Isaac" if gender == "boy":
        print("Target found!")
    case "yvette"|"bibiana" if gender == "girl":
        print("Target is close...")
    case _:
        print("cold!")

'''range method - with three parameters...the start included
...the end excluded..and the intervals in which to print them'''
for i in range(2, 50, 5):
    print(i)

#nested for loop
#use "pass" for empty for loops
a = ["red","pink","black"]
b = ["apple","melon","pear"]

for i in a:
    for x in b:
        print(i, x)

#functions
def myfunc(name):
    print("Hello, " + name + "!")
    
myfunc("jane")

#recursion