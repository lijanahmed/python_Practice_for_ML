#inheritance
#single lebel
class Car:
    def start(self):
        print( "car will start.")

    def Stop(self):
        print("stop the engine.")

    def Break(self):
        print("breaking the car.")

class Toyota(Car):
    # this has all property of car.
    def __init__(self,color):
        self.color=color
    
car1= Toyota("black toyota ")

car1.start()
car1.Break()
car1.Stop()

#multi lebel

class A:
    def __init__(self):
        pass
    def NameA(self):
        print("this is class A")

class B(A):
    def __init__(self):
        pass 
    def NmaeB(self):
        print("this is class B")
class C(B):
    def __init__(self):
        pass
    def NameC(self):
        print("this is the class C")
        super().NameA()

c=C()
c.NameA()
c.NmaeB()
c.NameC()
# call all the method of parents class using super(). 
