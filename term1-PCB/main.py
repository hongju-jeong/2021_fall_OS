import SchedulingQueue




def main():
    jobqueue = SchedulingQueue.JobQueue(10)
    readyqueue = SchedulingQueue.ReadyQueue(4)
    devicequeue = SchedulingQueue.DeviceQueue(1)
    jobqueue.enqueue(1)
    jobqueue.enqueue(2)
    jobqueue.enqueue(3)
    jobqueue.enqueue(4)
    jobqueue.enqueue(5)
    jobqueue.enqueue(6)
    jobqueue.enqueue(7)
    jobqueue.enqueue(8)
    jobqueue.enqueue(9)
    jobqueue.enqueue(10)


    

    readyqueue.enqueue(jobqueue.put_ready_queue_point,devicequeue)
    running_pcb = readyqueue.running(jobqueue.put_ready_queue_point,devicequeue)

    #phase1
    print(f'#PCB{running_pcb.id} - PID{running_pcb.id} Process Running')
    print(f'Running: PCB{running_pcb.id}')
    print(f'Ready:',end=" ")
    readyqueue.printQueue()
    print(f'Wait:')
    print(f'Job Queue:',end=" ")
    jobqueue.printQueue()
    print()

    devicequeue.enqueue(running_pcb)

    #phase2
    print(f'#PCB{running_pcb.id} - PID{running_pcb.id} HDD I/O Event')
    print(f'Running: ')
    print(f'Ready:',end=" ")
    readyqueue.printQueue()
    print(f'Wait:',end=" ")
    devicequeue.printQueue()
    print(f'(HDD I/O Queue)')
    print(f'Job Queue:',end=" ")
    jobqueue.printQueue()
    print()

    # readyqueue.enqueue(jobqueue.put_ready_queue_point,devicequeue)
    running_pcb = readyqueue.running(jobqueue.put_ready_queue_point,devicequeue)

    #phase3
    print(f'#PCB{running_pcb.id} - PID{running_pcb.id} HDD I/O Event')
    print(f'Running: PCB{running_pcb.id}')
    print(f'Ready:',end=" ")
    readyqueue.printQueue()
    print(f'Wait:',end=" ")
    devicequeue.printQueue()
    print(f'(HDD I/O Queue)')
    print(f'Job Queue:',end=" ")
    jobqueue.printQueue()
    print()



    #phase4
    print(f'#PCB{devicequeue.getIoPCBId()} - PID{devicequeue.getIoPCBId()} HDD I/O finished')
    devicequeue.ioFinished()
    print(f'Running: PCB{running_pcb.id}')
    print(f'Ready:',end=" ")
    readyqueue.printQueue()
    print(f'Wait:',end=" ")
    devicequeue.printQueue()
    print(f'(HDD I/O Queue)')
    print(f'Job Queue:',end=" ")
    jobqueue.printQueue()
    print()

    #phase5
    print(f'#PCB{running_pcb.id} - PID{running_pcb.id} Process Terminated')
    jobqueue.terminated(2)
    print(f'Running:')
    print(f'Ready:',end=" ")
    readyqueue.printQueue()
    print(f'Wait:',end=" ")
    devicequeue.printQueue()
    print(f'(HDD I/O Queue)')
    print(f'Job Queue:',end=" ")
    jobqueue.printQueue()
    print()

    running_pcb = readyqueue.running(jobqueue.put_ready_queue_point,devicequeue)

    #phase6
    print(f'#PCB{running_pcb.id} - PID{running_pcb.id} Process Running')
    print(f'Running: PCB{running_pcb.id}')
    print(f'Ready:',end=" ")
    readyqueue.printQueue()
    print(f'Wait:')
    print(f'Job Queue:',end=" ")
    jobqueue.printQueue()
    print()

if __name__ == "__main__":
    main()
    
