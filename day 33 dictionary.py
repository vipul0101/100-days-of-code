# formation of dictionary and how to access them
dict={
    544:"harry",
    36:"ritik",
    44:45,

}

print(dict[36])

# for accessing keys of a dictionary
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# again here is a catch while accessing the keys 
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.get('name2'))  #here this line gives output as none
print(info['name2'])  #here this line give error

#########

info = {'name':'Karan', 'age':19, 'eligible':True}

print(info.items())

for key, value in info.items():
    print(f"the value of the correspending key {key} is {value}")