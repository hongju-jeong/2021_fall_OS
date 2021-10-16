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


SJFQueue = []

SJFQueue.append(list[0])
del list[0]


time = 0

print(time)
print(f'P{SJFQueue[0].id} Process arrival')
print(f'P{SJFQueue[0].id} Process start')

endList = []

while(len(SJFQueue) >0):
    

    
    for i in list:
        if(i.arrival_time == time):
            print(f'P{i.id} Process arrival')
            SJFQueue.append(i)
            del i
            if(SJFQueue[0].burst_time>SJFQueue[-1].burst_time):
                temp = SJFQueue[0]
                SJFQueue[0] = SJFQueue[-1]
                SJFQueue[-1] = temp
                print(f'P{SJFQueue[0].id} Process start')

    
    for i in range(1,len(SJFQueue)-1):
        if(SJFQueue[i].burst_time > SJFQueue[-1].burst_time):
            temp = SJFQueue[i]
            SJFQueue[i] = SJFQueue[-1]
            SJFQueue[-1] = temp

    if(SJFQueue[0].burst_time == 0):
        print(f'P{SJFQueue[0].id} Process end')
        endList.append(SJFQueue[0])
        del SJFQueue[0]
        if(len(SJFQueue)!= 0):
            print(f'P{SJFQueue[0].id} Process start')


    for i in range(1,len(SJFQueue)):
        SJFQueue[i].waiting_time+=1

    
    time+=1
    if(len(SJFQueue)!= 0):
        SJFQueue[0].burst_time -= 1
        print(f'P{SJFQueue[0].id} : {SJFQueue[0].burst_time}')
        print(f'time: {time}')
    


sum_waiting_time = 0
for i in endList:
    sum_waiting_time += i.waiting_time

print(f'SJF average waiting time : {sum_waiting_time/6}')





    

