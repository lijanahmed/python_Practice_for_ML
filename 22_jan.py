class Lijan:
    identity= "visitor"
    # identity is same for everyone , so no need to make extra memory storage.
    def __init__(self,name):
        self.nm= name
        print(f"wecome {self.nm}, to my world.")

l1= Lijan("a")
print(l1.nm)
print(l1.nm , "is a ", Lijan.identity)

l2= Lijan("b")
print(l2.nm)
print(l2.nm , "is a ", Lijan.identity)

