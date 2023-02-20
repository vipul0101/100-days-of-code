# update a value in dictionary
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

#######
ep1={122:26, 15:55, 556:78, 69:44}
ep2={223:54, 448:557, 56:14}
ep1.update(ep2)
print(ep1)

#to clear a dict

ep2.clear()
print(ep2)

#pop an element
ep1.pop(122) #it removes the corresponding item
print(ep1)

#to delete the dict
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)  # this deletes the whole dict

