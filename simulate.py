import random
import Food
import Job
import Citizen

# create some food 
foods = []

for x in range(0,random.randint(10,100)):   # 10-100 apples 
    name = "Apple-{}".format(x)
    energy = random.randint(1,6) * 60       # 1-6 hours
    duration = 5 * (24 * 60)                # 5 days

    foods.append(Food.Food(name, energy, duration))

# create some work
jobs = []

for x in range(0,random.randint(10,100)):   # 10-100 jobs
    name = "Job-{}".format(x)
    duration = 8 * 60                       # 8 hours
    energy = 8 * 60                         # 8 hours worth of energy
    skills = []                             # not implemented
    tools = []                              # not implemented
    materials = []                          # not implemented
    products = []                           # not implemented

    jobs.append(Job.Job(name, duration, energy, skills, tools, materials, products))

# create some citizens
citizens = [] 

for x in range(0,random.randint(1,10)):             # 1-10 citizens
    name = "Charlie-{}".format(x)
    age = random.randint(18,75) * (365 * (24 * 60)) # 18-75 years old
    energy = random.randint(3,5) * (24 * 60)        # 3-5 days worth of energy 

    citizens.append(Citizen.Citizen(name, age, energy))

# start the simulation
print("{} Citizens, {} Pieces of food, {} Jobs".format(len(citizens), len(foods), len(jobs)))
raw_input("Press any enter to begin.")

# loop until they are all toast
dayidx = 0
last_food_day = None
last_job_day = None
graveyard = []

while len(citizens) > 0:

    print("Day {}".format(dayidx))

    for index, citizen in enumerate(citizens):
        
        if citizen.get_energy() > 0:

            # show status
            citizen.print_status()

            # eat
            if len(foods) > 0:
                citizen.eat(foods.pop())
            else:
                if not last_food_day:
                    last_food_day = dayidx
                    print("Out of food!")

            # work
            if len(jobs) > 0:
                citizen.work(jobs.pop())    # 8 hours of work
            else:
                citizen.age(60 * 8)         # 8 hours of idleness
                if not last_job_day:
                    last_job_day = dayidx
                    print("Out of jobs!")

            # leasure
            citizen.age(60 * 8)     # 8 hours of leasure

            # sleep
            citizen.sleep(60 * 8)   # 8 hours of sleep

        else:
            print("{} is dead.".format(citizen.get_name()))
            graveyard.append({"name": citizen.get_name(), "last_day": dayidx});
            citizens.pop(index)

    dayidx = dayidx + 1

print("Community terminated after {} days (last day of food: {}, last day of work: {}).".format(dayidx, last_food_day, last_job_day))

print("Citizen Statistics:")
for citizen in graveyard:
    print("{}: day {}".format(citizen["name"], citizen["last_day"]))
