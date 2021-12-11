class Optimal():

    def __init__(self):
        self.page_frame = []
        self.page_history = [1,2,1,4,5,6,3,4,6,3,7,3,1,5,3,7,3,4,2,4,1,4,5,1]
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
            history_temp = self.page_history
            #print("history_temp : " , history_temp)
            max_find = -1
            for index in self.page_frame:
                if(index in history_temp):
                    find = history_temp.index(index)
                else:
                    find = 9999
                if(find > max_find):
                    self.change_dict['num'] = index
                    self.change_dict['count'] = find
                    max_find = find

            change_index = self.page_frame.index(self.change_dict['num'])
            self.page_frame[change_index] = num
            self.count_page_faults += 1
            
            print(self.page_frame)
        self.page_history = self.page_history[1:]
    def printPageFaults(self):
        print("Count page faults : ",self.count_page_faults)

    

optimal = Optimal()


optimal.putItem(1)
optimal.putItem(2)
optimal.putItem(1)
optimal.putItem(4)
optimal.putItem(5)
optimal.putItem(6)
optimal.putItem(3)
optimal.putItem(4)
optimal.putItem(6)
optimal.putItem(3)
optimal.putItem(7)
optimal.putItem(3)
optimal.putItem(1)
optimal.putItem(5)
optimal.putItem(3)
optimal.putItem(7)
optimal.putItem(3)
optimal.putItem(4)
optimal.putItem(2)
optimal.putItem(4)
optimal.putItem(1)
optimal.putItem(4)
optimal.putItem(5)
optimal.putItem(1)

optimal.printPageFaults()