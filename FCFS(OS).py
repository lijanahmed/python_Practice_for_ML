# First come first serve

process=[]
arivalTime = []
burstTime = []
completionTime= []
tat= []
waitingTime= []

proNum= int(input("Enter the process number: "))

def getInput():
    
    for i in range(proNum):
        procName= input(f"Enter process{i+1} name: ")
        process.append(procName)
        arTime= int(input(f"Arival Time for {process[i]}: "))
        arivalTime.append(arTime)
        brTime= int(input(f"Burst Time for {process[i]}: "))
        burstTime.append(brTime)

def calculate():
    comTime=0
    for i in range(proNum):
        comTime+= burstTime[i]
        completionTime.append(comTime)

        tat.append(completionTime[i]- arivalTime[i])
        waitingTime.append(tat[i]- burstTime[i])

# def getCompletionTime ():
#     comTime=0
#     for i in range(proNum):
#         comTime+= burstTime[i]
#         completionTime.append(comTime)

# def turnAroundTime():

#    for i in range(proNum):
#        tatTime= completionTime[i]- arivalTime[i]
#        tat.append(tatTime)
       
# def getWaitingTime():
#     for i in range(proNum):
#         wTime= tat[i]- burstTime[i]
#         waitingTime.append(wTime)


def ShowAll():
    getInput()
    print(f"process are : {process}")
    print(f"araival time are : {arivalTime}")
    print(f"burst time are : {burstTime}")
    print(f"complition time are : {completionTime}")
    print(f"TAT time are : {tat}")
    print(f"Waiting time are : {waitingTime}")

def showResult():
    getInput()
    calculate()
    print("process   Arival Time   Burst Time   completion Time   TAT time   waiting Time ")
    for i in range(proNum):
        print(f"  {process[i]}           {arivalTime[i]}            {burstTime[i]}               {completionTime[i]}             {tat[i]}           {waitingTime[i]} ")


showResult()

