import random
import time
random.seed(3856)

#Class to creates nodes to be added to the queue
class Node:
    #This is the constructor 
    def __init__(self, data): 
        self.data = data
        self.next = None
  
#Class to create a singly linked list
class SinglyLinkedList: 
    #This is the constructor
    def __init__(self):
        self.head = None

    #Adds node to the start of the queue
    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    #Adds node to the end of the queue
    def append(self, data):
        NewNode = Node(data)
        #If it is the first node
        if self.head is None: 
            self.head = NewNode
            return
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  NewNode 
  
    #Adds node at the correct position in the queue
    def placement(self, data):
        position = self.head
        NewNode = Node(data)
        counter = -1
        while (position):
            if (position.data < data):
                position = self.head
                for i in range(counter):
                    position= position.next
                NewNode.next = position.next
                position.next = NewNode
                return
            else:
                position = position.next
                counter += 1
        Floors.append(data)
        return


    # Popping Values here    
    def pop(self, Floor):
        # print("The function pop")
        temp = self.head.next
        self.head = temp

    #Function to print the elements of the queue
    def Display(self):
        numbers = [] 
        temp = self.head 
        while (temp): 
            numbers.append(temp.data.FloorNumber) 
            temp = temp.next
        return numbers

    #Returns the size of the queue
    def Size(self): 
        temp = self.head 
        counter = 0
        while (temp):
            counter += 1  
            temp = temp.next
        return counter

class Floor:

    def __init__(self, FloorNumber, NoOfPassengers):
        self.Passengers = NoOfPassengers
        self.FloorNumber = FloorNumber

    def check(self):
        print("Floor ", self.FloorNumber, "P ", self.Passengers)


class Elevator:

    def __init__(self, GivenFloor,Enum):
        self.CurrentFloor = GivenFloor
        self.destined = 0
        self.Capacity = 0
        self.Steps = 0
        self.differ = 0
        self.Enum = Enum

    def check(self):
        print("Identifier",self.Enum, "CFloor ", self .CurrentFloor, "DFloor ", self.destined, "Cap ",self.Capacity)

    def boarder(self, Floor):
        while self.Capacity < 20 and Floor.Passengers != 0:
            self.Capacity += 1
            Floor.Passengers -= 1
        self.destined = Floor.FloorNumber

    def differential(self, Floor):
        diff = abs(self.CurrentFloor - Floor.FloorNumber)
        return diff


if __name__ == '__main__':

    FloorList = SinglyLinkedList()
    ElevatorList = [Elevator(5,2),Elevator(2,2),Elevator(8,2)]

    for i in range(1,20):
        gen = random.randint(0,1)
        if gen == 1 :
            p = random.randint(1,20)
            FloorList.append(Floor(i,p))

    # FloorList.append(Floor(3,5))
    # FloorList.append(Floor(6,5))
    # FloorList.append(Floor(9,5))

    i = 0 #Redefining
    TimeTaken = False

    print(FloorList.Display())

    while FloorList.Size() > 0:

        min = float("inf") #infinity
        flag = False
        temp = FloorList.head

        while temp:

            for i in ElevatorList:

                if i.CurrentFloor == temp.data.FloorNumber :
                    EleObj = i
                    FlrObj = temp.data
                    flag = True ## Flag Showing that we are ready to board hence breaking
                    break

                elif i.differential(temp.data) < min :
                    EleObj = i
                    FlrObj = temp.data
                    min = i.differential(temp.data)

            if flag: # Breaking again for same reason
                break

            if time.clock() > 10 and TimeTaken == False:
                for i in range(1,10):
                    p = random.randint(1,20)
                    FloorList.append(Floor(i,p))
                TimeTaken = True

            temp.data.check()
            temp = temp.next
        
        EleObj.CurrentFloor = FlrObj.FloorNumber
        EleObj.boarder(FlrObj)

        if EleObj.Capacity == 20:
            EleObj.CurrentFloor = 0
            EleObj.Capacity = 0

        if FlrObj.Passengers == 0: # Removing Floor Object
            # print("POP")
            FloorList.pop(FlrObj)


        for i in ElevatorList:
            i.check()

    print(FloorList.Display())
    print("Time taken by the program", time.clock())