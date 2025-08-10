'''first method of opening a file
which requires you to use the close method'''
f = open("game.py")
print(f.read())
f.close()

'''Second method using with
which take care of closing the file 
hence don't have to use the close method'''
with open("game.py") as f:
    print(f.readline())
    
#using for loop to print each character in the file
with open("game.py") as f:
    for x in f:
        print(x)
        
#open a file and add content by using "a = append"
with open("game.py", "a") as f:
    f.write("#more content")
    
with open("game.py") as f:
    print(f.read())
#open a file and add content by using "w = overwrite"
with open("game.py", "w") as f:
    f.write("#opps! You deleted the content in this file")

with open("game.py") as f:
    print("f.read")
    
x = open("don.py", "x")