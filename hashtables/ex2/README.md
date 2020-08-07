# One-Way Flight Trip

You've booked a _really_ cheap one-way flight. Unfortunately, that means
you have _tons_ of layovers before you reach your destination. The
morning of, you woke up late and had to scramble to the airport to catch
your first flight. However, in your rush, you accidentally scrambled all
your flight tickets. You don't know the route of your entire trip now!

Write a function `reconstruct_trip` to reconstruct your trip from your
mass of flight tickets. Each ticket is represented as a class with the
following form:

```
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
```

where the `source` string represents the starting airport and the
`destination` string represents the next airport along our trip. The
ticket for your first flight has a destination with a `source` of
`NONE`, and the ticket for your final flight has a `source` with a
`destination` of `NONE`. 

Pseudocode for an array of `Tickets` might look like this:

```
tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
```

Your function should output an array of strings with the entire route of
your trip. For the above example, it should look like this:

```
["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
```

Your solution should run in linear time. You can assume that your
function will always be handed a valid ticket chain as input. 

## Hints

* The crux of this problem requires us to 'link' tickets together to
  reconstruct the entire trip. For example, if we have a ticket `('SJC',
  'BOS')` that has us flying from San Jose to Boston, then there exists
  another ticket where Boston is the starting location, `('BOS',
  'JFK')`. 

* We can hash each ticket such that the starting location is the key and
  the destination is the value. Then, when constructing the entire
  route, the `i`th location in the route can be found by checking the
  hash table for the `i-1`th location.

* U --> Want a list of destinations only. 
* P --> 
    XXXXXXXXXXXXXX SECOND ATTEMPT XXXXXXXXXXXXXXXXXXXXXXXX
    # initialize route list
    # initialize dict
    # 1. Store tickets in a dict
        # Loop over ticket in tickets
        # print(ticket.source, ticket.destination)
        # Key: Source, Value: Destination
    # 2. Initialize stop variable
    # 3. Pick a start point of destination 'NONE'
        # Looks like the start point in the tests has 'NONE' as the source. Only one 'NONE' as source (start point) and one 'NONE' as destination (stop point)
    # 4. While loop, like Markov example from lecture. 
    # While not stopped
        # if the len(route) is matches the length variable
            # change stop variable to true
        # check if destination is in route list
            # Yes, change start point to next variable
            # No, append destination to route list
    # 5. Return the route list

    XXXXXXXXXXXXXX FIRST ATTEMPT XXXXXXXXXXXXXXXXXXXXXXXX
    # initialize route list
    # initialize dict
    # 1. Store tickets in a dict
        # Loop over ticket in tickets
            # Key: Source, Value: Destination
    # 2. Pick start point and stop point
        # Looks like the start point in the tests has 'NONE' as the source. Only one 'NONE' as source (start point) and one 'NONE' as destination (stop point)
    # 3. Use a while loop like the Markov chain form lecture
        # While destination is not 'NONE' move to the next ticket and append the destination to the route list
    # 4. When destination is 'NONE' stop
    # 5. Return the route list
* E --> ✅
* R --> Could this pattern be used for the file names problem? 

 