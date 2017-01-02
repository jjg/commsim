import sys
import Citizen
import Activity

# initialize community
community = {"living_citizens":[],"deceased_citizens":[],"activities":[],"goods":[]}

# initialize citizens
jason = Citizen.Citizen("Jason", (20 *((60*24)*365)), 100, 100, 10)
community["living_citizens"].append(jason)

# initialize activities 
read_a_book = Activity.Activity("Reading a book", (60 * 12), 0, 0, 1, ["Reading"], ["Book"], None, ["Knowledge"])
community["activities"].append(read_a_book)

# TODO: initialize goods

# increment minute until all citizens are gone
minute = 1 
while len(community["living_citizens"]) > 0:
    # select citizen
    for index, citizen in enumerate(community["living_citizens"]):

        # display citizen status
        citizen.print_status()

        # get the citizen's status
        citizen_status = citizen.get_status()

        # if deceased, move to cemetary
        if(citizen.get_PE() < 1):
            community["deceased_citizens"].append(citizen)
            community["living_citizens"].pop(index)

        else:

            # if hungry, eat
            if citizen_status.hungry:
                print("hungry")
                # TODO: infinate apples should be replaced by scarce goods
                eat_apple = Activity.Activity("Eating an apple", 15, -5, 0, 0, None, None, None, None)
                citizen.add_activity(eat_apple)

            # if tired, sleep
            if citizen_status.tired:
                print("tired")
                sleeping = Activity.Activity("Sleeping", (8 * 60), -2, -2, -2, None, None, None, None)
                citizen.add_activity(sleeping)

            # if idle, work
            if citizen_status.idle:
                if len(community["activities"]) > 0:
                    citizen.add_activity(community["activities"].pop())
                else:
                    print("No activities left")
                    sys.exit(0)

            # age citizen one minute
            citizen.age(1)

    minute = minute + 1

# TODO: display status of community 
