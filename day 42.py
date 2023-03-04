#HERE WE ARE LEARNING ABOUT ENUMERATE FUNCTION

marks = [20,33,35,65,68,98,88,44,52,12]

index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("VIP, awesome")
    index +=1
    
#FOR MAKING IT SHORT WE USE ENUMERATE FUNCTION AS FOLLOWS

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("you are great")