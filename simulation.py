import copy

rows = 10

# represents a person who is going to board the plane
class Person:
    delay = None
    seat_assignment = None
    seat_time = None

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
            self.behind = node
        else:
            self.behind.add_to_end(node)

    def add_person_to_node(self, person):
        self.passenger = person

    # ticks this cell, moving the person it may or may not contain as appropriate
    def single_tick():
        pass
        
    # represents the current state of this aisle node as a string
    def to_string(self):
        if self.passenger:
            return 'X'
        else:
            return '-'



# represents a list of aisle cells for a certain number of rows in an airplane
class Aisle:
    head = None

    # initializes an aisle of given number of rows (nodes)
    def __init__(self, rows):
        self.head = AisleNode(0)
        
        for i in range(rows - 1):
            self.head.add_to_end(AisleNode(i))

    # represents the current state of this aisle as a string
    def __str__(self):
        output = ''
        current_node = self.head
        while current_node:
            output += ' --> ' + current_node.to_string()
            current_node = current_node.behind
        return output
        

    # initializes one time-unit of movements throughout the aisle. individuals will move as appropriate when possible during the tic
    def onTick():
    
        pass

    # returns the last node in the linked list
    def get_last_node(self):
        last_node = self.head

        while last_node.next:
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



def simulate_seating(_passengers):
    passengers = copy.deepcopy(_passengers) # make a copy we can mutate

    all_passengers_seated = False

    aisle = Aisle(rows)
    print(aisle)

    # FOR NOW, just count number of ticks needed to seat the plane in full
    tickCount = 0

    # continue to seat passengers until everyone is in their seats
    while not all_passengers_seated and not aisle.empty():
        current_row = aisle.get_last_node()

        # one tic is going through the aisle and making appropriates updates to passenger positions 
        while current_row:

            # check to see if this aisle position has a passenger
            if current_row.passenger != None:

                # check if we can seat this passenger in the current row 
                if current_row.passenger.seat_assignment == current_row.row:
                    # this is where we need to pause the simulation for the number of ticks 

                    current_row.passenger.seat_time(tickCount) # set the time that the passenger sat at 
                    current_row.passenger = None # remove person from aisle
                else:
                    # if we can move this person forward, move them forward and remove them from the current aisle position
                    if current_row.behind and current_row.behind.passenger == None:
                        current_row.behind.passenger = current_row.passenger
                        current_row.passenger = None
                
                # if we are looking at the first aisle position and its empty, 
            current_row = current_row.ahead

        tickCount += 1
        
    return tickCount


p1 = Person(3, 2)
p2 = Person(3, 3)
p3 = Person(3, 4)
p4 = Person(3, 1)
p5 = Person(3, 1)

passengers = [p1, p2, p3, p4, p5]
print(simulate_seating(passengers))