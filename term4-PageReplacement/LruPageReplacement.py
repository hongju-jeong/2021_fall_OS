class LRU():
    def __init__(self):
        self.page_frame = []
        self.page_history = []
        self.change_dict = {'num':-1,'count':-1}
        self.count_page_faults = 0
    def putItem(self, num):
        if(num in self.page_frame):
            pass
        elif(len(self.page_frame)<4):
            self.page_frame.append(num)
            self.count_page_faults += 1
            print(self.page_frame)
        else:
            history_temp = list(reversed(self.page_history)) 
            #print("history_temp : " , history_temp)
            max_find = -1
            for index in self.page_frame:              
                find = history_temp.index(index)
                if(find > max_find):
                    self.change_dict['num'] = index
                    self.change_dict['count'] = find
                    max_find = find

            change_index = self.page_frame.index(self.change_dict['num'])
            self.page_frame[change_index] = num
            self.count_page_faults += 1
            
            print(self.page_frame)
        self.page_history.append(num)
    def printPageFaults(self):
        print("Count page faults : ",self.count_page_faults)


lru = LRU()

lru.putItem(1)
lru.putItem(2)
lru.putItem(1)
lru.putItem(4)
lru.putItem(5)
lru.putItem(6)
lru.putItem(3)
lru.putItem(4)
lru.putItem(6)
lru.putItem(3)
lru.putItem(7)
lru.putItem(3)
lru.putItem(1)
lru.putItem(5)
lru.putItem(3)
lru.putItem(7)
lru.putItem(3)
lru.putItem(4)
lru.putItem(2)
lru.putItem(4)
lru.putItem(1)
lru.putItem(4)
lru.putItem(5)
lru.putItem(1)

lru.printPageFaults()


            


        

        