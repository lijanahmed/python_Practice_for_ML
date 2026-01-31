# privet method ( __ )
class Account:
    def __init__(self, acc_no,acc_pass):
        # self.acc_pass= acc_pass
        self.acc_no= acc_no
        # here password is  privet but everyone can control 
# now 
        
        self.__acc_pass= acc_pass # this is privet

    def reset_pass(self,newPass):
        self.__acc_pass= newPass

acc1=Account(1234,"lijan11223344")
print(acc1.acc_no)
# acc1.__acc_pass

#done privet public.