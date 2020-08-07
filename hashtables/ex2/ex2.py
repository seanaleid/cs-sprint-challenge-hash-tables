#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    def __repr__(self):
        return f"Source: {self.source}, Destination: {self.destination}"


def reconstruct_trip(tickets, length):
    # initialize route list
    route = []
    # initialize dict
    d = dict()
    
    # 1. Store tickets in a dict
    # Loop over ticket in tickets
    for ticket in tickets:
        # print(ticket.source, ticket.destination)
        # Key: Source, Value: Destination
        d[ticket.source] = ticket.destination
    
    # 2. Initialize stop variable
    destination = False
    # 3. Pick a start point of destination 'NONE'
    flight = d['NONE']

    # 4. While loop, like Markov example from lecture. 
    # While not stopped
    while not destination: 
        # if the len(route) is matches the length variable
        if len(route) == length: 
            # change stop variable to true
            destination = True
        # check if destination is in route list
        elif flight in route:
            # Yes, change start point to next variable
            flight = d[flight]
        else:
            # No, append destination to route list
            route.append(flight)
    # 5. Return route list
    return route
