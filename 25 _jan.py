class Student:
    def __init__(self,name, mark1):
        self.name=name
        self.totalMark= 0
        for i in mark1:
            self.totalMark+=i

    def avg_mark(self):
        avg = self.totalMark / 3
        print( f"hi {self.name} your avg mark is: { avg}")
    @staticmethod
    def hello():
        print ("hello!")
        
s1=Student("Shakib",[12,13,14])
s2= Student("rakib",[21,22,23])
s1.avg_mark()
s1.hello()
s2.avg_mark()
s2.hello()


#sattic method  done
#Abstraction 
print( "now learning the abstruction")

class car:
    def __init__(self):
        self.acc= False
        self.brk= False
        self.clutch= False
    def Start(self):
        self.clutch= True
        self.acc= True
        print( "car started")
    def Stop(self):
        self.clutch= False
        self.acc=False
        self.brk= True
        print("car is stop.")

cr=car()
cr.Start()
cr.Stop()

# practice
class BankAcc:
    def __init__(self,accnum,balance):
        self.accNum=accnum
        self.balance= balance
    def debit(self, amount):
        self.balance-=amount
        print(f"{amount} BDT was debited.")
    def credit(self, amount):
        self.balance+=amount
        print(f"{amount} BDT was credited.")
    def checckBal(self):
        print(self.balance)    

acc=input("input account num:")
bal=int(input("inpu Balance  num:"))

customer1= BankAcc(acc,bal)
customer1.credit(1000)
customer1.debit(200)
customer1.checckBal()





