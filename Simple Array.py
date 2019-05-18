import random
import time
random.seed(3856)

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

    def differential(self, Floor):
        diff = abs(self.CurrentFloor - Floor.FloorNumber)
        return diff


def gen():
    return random.randint(0,1)


if __name__ == '__main__':

    # FloorList = [Floor(6,3),Floor(7,3),Floor(9,3)]
    ElevatorList = [Elevator(8,1),Elevator(8,2),Elevator(8,3)]
    FloorList = []
    for i in range(2000):
        if gen() == 1 :
            p = random.randint(0,20)
            FloorList.append(Floor(i,p))

    prevmin = 0
    i = 0
    TimeTaken = False
    while len(FloorList)!=0:

        mins = float("inf")
        flag = False


        for j in FloorList:

            for i in ElevatorList:

                prevmin = i.differential(j)
                if i.CurrentFloor == j.FloorNumber :

                    EleObj = i
                    FlrObj = j
                    flag = True ## Flag Showing that we are ready to board hence breaking
                    break

                elif i.differential(j) < mins or (prevmin == i.differential(j) and gen() == 1) :

                    i.destined = j.FloorNumber
                    EleObj = i
                    FlrObj = j
                    mins = i.differential(j)
                    prevmin = mins

            if flag: # Breaking again for same reason
                break
            if time.process_time() > 10 and TimeTaken == False:
                for i in range(1,10):
                    p = random.randint(1,20)
                    FloorList.append(Floor(i,p))
                TimeTaken = True

        EleObj.CurrentFloor = FlrObj.FloorNumber
        EleObj.boarder(FlrObj)

        # for j in FloorList:
        #     j.check()

        if EleObj.Capacity == 20:
            EleObj.CurrentFloor = 0
            EleObj.Capacity = 0


        if FlrObj.Passengers == 0: # Removing Floor Object
            FloorList.remove(FlrObj)

        for i in ElevatorList:
            i.check()

    print("Time taken by program:", time.process_time())