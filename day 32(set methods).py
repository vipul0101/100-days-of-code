#combination of two sets
s1 = {2,3,4,5,6}
s2 = {4,6,7,8,9}
print(s1.union(s2))
# we can update a set acc to the second one
s1.update(s2)
print(s1)

# for getting common values among both sets
## here since i updated s1 so we got s1={2, 3, 4, 5, 6, 7, 8, 9} and now with this we have to do the intersection 
s3 = s2.intersection(s1)
print(s3)
#this is another example for showing intersection (comman set)
cities = {"Tokyo", "Madrid", "Berlin", 5, "Delhi"}
cities2 = {"Tokyo", 5, 6, "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

#again for update using intersection command
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

#now our cities set updated permanently and further operations are done with the same set

#again for getting uncommen elements from sets we use symmetric_difference command
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

#now for update the set using symettric difference
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

#to find difference btw two sets or we can say to get values that are in one set and not in second one
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

#again for update the set we use
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))

#disjoint sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

#superset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

#subset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

#add
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

#update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

#remove/discard
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)

#pop
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#del
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

#clear
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# to check item existence
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")