
#tuple
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[1])
for i in thistuple:
    print(i)

thistuple = ("apple", "banana", "cherry")
y= list(thistuple)
y.remove("banana")
thistuple= tuple(y)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisdict=dict(name = "John", age = 36, country = "Norway")
print(thisdict)
thisdict["Lijan"]= "CSE student"
print(thisdict)
print(thisdict["Lijan"])

allkey = thisdict.keys()
allvalue = thisdict.values()

print(allkey, allvalue)
