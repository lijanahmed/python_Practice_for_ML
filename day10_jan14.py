class Lijan:
    def __init__(self): # this is a constrictor      
        name= "LIJAN"
        print("the coder is ",name)
        # print(self)
 

ljn= Lijan()

# print(ljn)

class Student:
    # def __init__(self):
    #     print("this is the defult cons.")

    # def __init__(self,nam):
    #     self.nam = nam
    #     print(self.nam)
    #     print(nam)
    name="abc colg"
    def __init__(self,nam,roll):
        self.nam = nam
        self.roll= roll
        print(self.nam,self.roll)
        
        
# x= input("inter the new student name here :")
s1=Student("x",1000)
# y= input("inter the new student name here :")
s2=Student("y",1100)

s3= Student("xy",1099)
print(s1.name)
