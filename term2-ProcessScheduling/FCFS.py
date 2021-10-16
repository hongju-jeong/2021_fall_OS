class Process:
    def __init__(self,_id,_arrival_time,_burst_time):
        self.id = _id
        self.arrival_time = _arrival_time
        self.burst_time = _burst_time
        self.waiting_time = 0


list = []

p1 = Process(1,0,10)
p2 = Process(2,3,12)
p3 = Process(3,7,4)
p4 = Process(4,10,6)
p5 = Process(5,14,8)
p6 = Process(6,15,7)


list.append(p1)
list.append(p2)
list.append(p3)
list.append(p4)
list.append(p5)
list.append(p6)


FCFSQueue = []

FCFSQueue.append(list[0])
del list[0]

time = 0
print(time)
print(f'P{FCFSQueue[0].id} Process arrival')
print(f'P{FCFSQueue[0].id} Process start')

endList = []



while(len(FCFSQueue) >0):
    for i in list:
        if(i.arrival_time == time):
            print(f'P{i.id} Process arrival')
            FCFSQueue.append(i)
            del i

    

    if(FCFSQueue[0].burst_time == 0):
        print(f'P{FCFSQueue[0].id} Process end')
        endList.append(FCFSQueue[0])
        del FCFSQueue[0]
        if(len(FCFSQueue)!= 0):
            print(f'P{FCFSQueue[0].id} Process start')

    for i in range(1,len(FCFSQueue)):
        FCFSQueue[i].waiting_time+=1

    time+=1
    if(len(FCFSQueue)!= 0):
        FCFSQueue[0].burst_time -= 1
        print(time)
    


sum_waiting_time = 0
for i in endList:
    sum_waiting_time += i.waiting_time

print(f'FCFS average waiting time : {sum_waiting_time/6}')





    

