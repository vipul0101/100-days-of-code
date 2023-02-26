#here we are learning about how to handle the error
a = input("enter the number :")

print(f"Multiplication table of {a} is: ")

for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")

# but if I give input as a string then it will give error 
# and now for handling the error we use some process like this shown below

a = input("enter the number :")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as e:
    print("this is invalid input error")

print('your code gives an error')
print("please change your lines")