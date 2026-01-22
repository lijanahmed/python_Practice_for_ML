
day = 4 
month = "januarry"
match day:
    case 1 if month== "januarry":
        print("day 1")
    case 2:
        print("day 2")
    case 3:
        print("day 3")
    case 4 if month== "januarry":
        print("day 4")
    case 5:
        print("day 5")
    case _:
        print("none")

match day:
    case 1|2|3|4 :
        print("this is a working day.") 

i = 0
while i < 6:
    i += 1
 
    if i == 3:
        continue
    print(i)
