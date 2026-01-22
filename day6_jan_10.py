def func(n):
    if n==0:
        return None
    else:
        print(n)
        func(n-1)

func(5)