import copy
import random

# represents a person who is going to board the plane
class Person:
    delay = None
    seat_assignment = None
    seat_time = None
    id = random.randint(100, 999) #random 3 digit id

    def __init__(self, delay, seat_assignment):
        self.delay = delay
        self.seat_assignment = seat_assignment

    # checks to see if the person is in their respective seat
    def isInSeat(self, row):
        if self.seat_assignment == row:
            return True
        else :              
            return False
    
    # sets the time that the passenger was sat at
    def seat_time(self, time):
        self.seat_time = time

    def __str__(self):
        return str(self.id)

# represents a position node in the aisle linked list
class AisleNode:
    ahead = None
    behind = None
    passenger = None
    
    def __init__(self, row):
        self.row = row

    # adds a new node behind the current node in the plane
    def add_to_end(self, node):
        if (self.behind == None):
            node.ahead = self
            self.behind = node
        else:
            self.behind.add_to_end(node)

    # updates this node to now reference the given person
    # IMPORTANT: throws an error if this already references a person.
    def add_person_to_node(self, person):
        if self.person != None:
            self.passenger = person
        else:
            return ValueError
        
    # represents the current state of this aisle node as a string
    def to_string(self):
        if self.passenger:
            # return 'X'
            return str("(" + str(self.passenger.delay) + "," + str(self.passenger.seat_assignment) + ")")
        else:
            return '_'

# represents a list of aisle cells for a certain number of rows in an airplane
class Aisle:
    head = None

    # initializes an aisle of given number of rows (nodes)
    def __init__(self, rows):
        self.head = AisleNode(0)
        
        for i in range(1, rows):
            self.head.add_to_end(AisleNode(i))

    # represents the current state of this aisle as a string
    def __str__(self):
        output = ''
        current_node = self.head
        while current_node:
            output += ' -> ' + current_node.to_string()
            current_node = current_node.behind
        return output

    # returns the last node in this aisle
    def get_last_node(self):
        last_node = self.head

        while last_node.behind:
            last_node = last_node.behind
        
        return last_node
    
    # returns true if no one is in the aisle 
    def empty(self):
        current_node = self.head

        while current_node:
            if current_node.passenger != None:
                return False
            current_node = current_node.behind
        
        return True

# returns the maximum row observed among the list of passengers
def getMaxRow(passengers):
    maxRow = 0
    for passenger in passengers:
        if passenger.seat_assignment > maxRow:
            maxRow = passenger.seat_assignment
    
    return maxRow

# runs a full simulation of seating the given list of passengers, seating them in the order in which they were supplied to the function
def simulate_seating(passengers):
    passengers = copy.deepcopy(passengers) # make a copy we can mutate

    all_passengers_seated = False

    # runs a simulation/builds aisle using number of rows needed based on list of passengers' seat assignments
    numRowsNeeded = getMaxRow(passengers)
    aisle = Aisle(numRowsNeeded)

    # FOR NOW, just count number of ticks needed to seat the plane in full
    tickCount = 0

    # continue to seat passengers until everyone is in their seats
    while not all_passengers_seated:
        current_row = aisle.get_last_node()

        print(aisle)
        print()

        # one tic is going through the aisle and making appropriates updates to passenger positions 
        while current_row:

            # check to see if this aisle position has a passenger
            if current_row.passenger != None:

                # check if we can seat this passenger in the current row 
                if current_row.passenger.seat_assignment == current_row.row:

                    # this is where we need to pause this persons ability to enter the row to create slow downs
                    if current_row.passenger.delay == 0:
                        current_row.passenger.seat_time(tickCount) # set the time that the passenger sat at 
                        current_row.passenger = None # remove person from aisle
                    else:
                        current_row.passenger.delay -= 1
                else:
                    # if we can move this person forward, move them forward and remove them from the current aisle position
                    if current_row.behind and current_row.behind.passenger == None:
                        current_row.behind.passenger = current_row.passenger
                        current_row.passenger = None
                
            # if we are looking at the first node in the aisle (first aisle position) add in a new passenger to the linked list
            if current_row.row == 0: 
                # if there are no more passengers to add 
                if len(passengers) < 1:
                    return tickCount

                # add passenger to aisle linked list
                if current_row.passenger == None:
                    current_row.passenger = passengers.pop(0)

            current_row = current_row.ahead

        tickCount += 1

    return tickCount

# # # Person (delay, row)
# # p1 = Person(3, 0)
# # p2 = Person(3, 3)
# # p3 = Person(3, 4)
# # p4 = Person(3, 1)
# # p5 = Person(3, 1)

# # passengers = [p1, p2, p3, p4, p5]

# randPassengers = []

# for i in range(90):
#     randPassengers.append(Person(random.randint(0, 8), int(i / 3)))

# random.shuffle(randPassengers)

# # print(getMaxRow(passengers))
# # print(simulate_seating(passengers))
# print(simulate_seating(randPassengers))