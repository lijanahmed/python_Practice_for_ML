def myfunction():
    x=20
    y=35
    print(f"the ans is : {x+y}")
myfunction()

def parameter(a):
    print(a)

def parameter2(*a):
    print(a)
    print(a[0])
    print(a[1])

parameter2(1,2,3,4)

#max number finding 
def maxx(*numbers):
    if len(numbers)==0:
        return None
    else:
        max= numbers[0]
        for i in range(len(numbers)):
            if numbers[i] > max:
                max=numbers[i]
    print(f"the max number among {numbers} \n is : {max}")
    
maxx(1,2,3,1,3,56,74,34,2,4,55,99,45,67,89)
