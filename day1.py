# end parametter
# print( " i am Lijan and my ambision is fulfil the goal.", end="")
# print(" for this i have to done so many work.")
# #type casting
# f= int(3.5) 
# x= str(3)
# a="Lijan"
# print(a, f, x)
# print(type(f), type(a), type(x))
# #Variable names are case-sensitive 

# #list
# [x, y, z] = ["apple", "banana", "cherry"]
# print(x)
# print(y)
# print(z)

# import random 
# print(random.randrange(20,30))

# if True:
#     print("lijan")
# txt = " i am a student."
# if "a" in txt :
#     print( "yeap a is here.")
# thislist = ["apple", "banana", "cherry"]
# for i in thislist:
#     print(i)

# thislist.insert(2,"a")
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# thislist.clear()
print(thislist)

newlsit= []
for i in thislist:
    if i!= "banana":
        newlsit.append(i)
    else :
        newlsit.append("orange")
print(newlsit)

newlsit=[ i if i!= "banana" else "orange" for i in thislist]
print(newlsit)

newnewlist=[i for i in thislist if "a" in i]
print(newnewlist)
