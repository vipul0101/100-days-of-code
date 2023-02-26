#here we are learning about how to handle the error
a = input("enter the number :")

print(f"Multiplication table of {a} is: ")

for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
