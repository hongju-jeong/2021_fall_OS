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


RRQueue = []

RRQueue.append(list[0])
del list[0]


time = 0
time_quantum = 0
print(time)
print(f'P{RRQueue[0].id} Process arrival')
print(f'P{RRQueue[0].id} Process start')

endList = []

while(len(RRQueue) >0):
    
    

    for i in list:
        if(i.arrival_time == time):
            print(f'P{i.id} Process arrival')
            RRQueue.append(i)
            del i

    if (time_quantum == 3):
        if(RRQueue[0].burst_time ==0):
            print(f'P{RRQueue[0].id} Process end')
            endList.append(RRQueue[0])
            del RRQueue[0]
            time_quantum = 0
            if(len(RRQueue)!= 0):
                print(f'P{RRQueue[0].id} Process start')

        else: 
            temp = RRQueue[0]
            del RRQueue[0]
            RRQueue.append(temp)
            print(f'P{RRQueue[0].id} Process start')
            time_quantum = 0
    
    

    
    if(RRQueue[0].burst_time == 0):
        print(f'P{RRQueue[0].id} Process end')
        endList.append(RRQueue[0])
        del RRQueue[0]
        time_quantum = 0
        if(len(RRQueue)!= 0):
            print(f'P{RRQueue[0].id} Process start')


    for i in range(1,len(RRQueue)):
        RRQueue[i].waiting_time+=1

    
    time+=1
    time_quantum+=1
    if(len(RRQueue)!= 0):
        RRQueue[0].burst_time -= 1
        print(f'time: {time}, time_quantum: {time_quantum}')
    


sum_waiting_time = 0
for i in endList:
    sum_waiting_time += i.waiting_time

print(f'RR average waiting time : {sum_waiting_time/6}')





    

