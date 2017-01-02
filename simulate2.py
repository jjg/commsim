import Citizen
import Activity

# initialize community
community = {"living_citizens":[],"deceased_citizens":[],"activities":[],"goods":[]}

# initialize citizens
jason = Citizen.Citizen("Jason", (20 *((60*24)*365)), 100, 100, 100)
community["living_citizens"].append(jason)

# initialize activities 
sleeping = Activity.Activity("Sleeping", (8 * 60), 1, 1, 1, None, None, None, None)
community["activities"].append(sleeping)

# TODO: initialize goods

# increment minute until all citizens are gone
minute = 1 
while len(community["living_citizens"]) > 0:
    # select citizen
    for index, citizen in enumerate(community["living_citizens"]):

        # display citizen status
        citizen.print_status()

        # if deceased, move to cemetary
        if(citizen.get_PE() < 1):
            community["deceased_citizens"].append(citizen)
            community["living_citizens"].pop(index)

        else:
            # TODO: if hungry, eat
            # TODO: if tired, sleep
            # TODO: if idle, work
            # TODO: age citizen one minute
            citizen.age(1)

    minute = minute + 1

# TODO: display status of community 
