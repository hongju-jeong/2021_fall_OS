class PCB:
    def __init__(self, _id, _state):
        self.id = _id
        self.next = None
        self.state = _state

class JobQueue:
    def __init__(self, _size):
        self.size = _size
        self.head = PCB(-1,"dummy")
        self.tail = PCB(-1,"dummy")
        self.num_of_data = 0
        self.put_ready_queue_point = PCB(-1,"dummy")
        self.fork_list = []

    def printReadyQueuePoint(self):
        print(self.put_ready_queue_point.next.id)

    def enqueue(self,pcb_id):
        if(self.num_of_data == self.size):
            print("JobQueue is full")
        else:
            new_pcd = PCB(pcb_id, "new")
            
            if(self.num_of_data == 0):
                self.head.next = new_pcd
                self.tail.next = new_pcd
                self.put_ready_queue_point.next = new_pcd
            else:
                self.tail.next.next = new_pcd
                self.tail.next = new_pcd
            
            
            self.fork_list.append(pcb_id)

            self.num_of_data += 1

    def terminated(self,pcb_id):
        if(self.num_of_data == 0):
            print("JobQueue is empty")
        else:
            terminate_point = self.head
            if(self.num_of_data == 0):
                pass
            else:
                while(terminate_point.next.id != pcb_id and terminate_point.next !=None):
                    terminate_point = terminate_point.next
                if(terminate_point.next.id == pcb_id):
                    terminate_point.next = terminate_point.next.next
                    if(terminate_point.next == None):
                        self.tail.next = terminate_point
                    
                    self.fork_list.remove(pcb_id)
                    self.num_of_data -= 1


    def printQueue(self):
        for i in self.fork_list:
            print(f'PCB{i}',end=" ")
        print()


            

class ReadyQueue:
    def __init__(self, _size):
        self.size = _size
        self.head = PCB(-1,"dummy")
        self.tail = PCB(-1,"dummy")
        self.num_of_data = 0

    def running(self,job_queue_ready_point,device_queue):
        running_pcb = self.head.next
        running_pcb.state = "running"
        self.head.next = self.head.next.next
        self.num_of_data -= 1
        self.enqueue(job_queue_ready_point,device_queue)
        return running_pcb

    def enqueue(self,job_queue_ready_point,device_queue):
        while(self.num_of_data<self.size):
            if(device_queue.is_io_finished == True):
                if(self.num_of_data == 0):
                    self.head.next = device_queue.put_ready_queue_point
                    self.tail.next = device_queue.put_ready_queue_point
                    self.head.next.state = "ready"
                    device_queue.put_ready_queue_point = None
                    device_queue.is_io_finished = False
                    device_queue.moveToHead()
                else:
                    self.tail.next.next = device_queue.put_ready_queue_point
                    self.tail.next = device_queue.put_ready_queue_point
                    self.tail.next.state = "ready"
                    device_queue.put_ready_queue_point = None
                    device_queue.is_io_finished = False
                    device_queue.moveToHead()

            elif(self.num_of_data == 0):
                self.head.next = job_queue_ready_point.next
                self.head.next.state = "ready"
                self.tail.next = job_queue_ready_point.next
                job_queue_ready_point.next = job_queue_ready_point.next.next

            else:
                self.tail.next.next = job_queue_ready_point.next
                self.tail.next = job_queue_ready_point.next
                self.tail.next.state = "ready"
                job_queue_ready_point.next = job_queue_ready_point.next.next
            self.num_of_data +=1

    def printQueue(self):
        print_point = self.head.next
        while(print_point.state == "ready"):
            print(f'PCB{print_point.id} ', end=" ")
            print_point = print_point.next
        print()

class DeviceQueue:
    def __init__(self, _size):
        self.size = _size
        self.head = PCB(-1,"dummy")
        self.tail = PCB(-1,"dummy")
        self.num_of_data = 0
        self.is_io_finished = False
        self.put_ready_queue_point = None
        

    def enqueue(self,running_pcb):
        if(self.num_of_data == self.size):
            print("DeviceQueue is full")
        else:            
            if(self.num_of_data == 0):
                self.head.next = running_pcb
                self.tail.next = running_pcb
                self.head.next.state = "wait"
            else:
                self.tail.next.next = running_pcb
                self.tail.next = running_pcb
                self.tail.next.state = "wait"

            self.num_of_data += 1

    def ioFinished(self):

        if(self.num_of_data == 0):
            print("DeviceQueue is empty")
        else:
            self.put_ready_queue_point = self.head.next
            self.is_io_finished = True

    def moveToHead(self):
        self.head.next = self.head.next.next

    def getIoPCBId(self):
        return self.head.next.id


    def printQueue(self):
        print_point = self.head.next
        while(print_point.state == "wait"):
            print(f'PCB{print_point.id} ', end=" ")
            print_point = print_point.next
