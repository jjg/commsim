import sys
import random
import Food
import Job
import Citizen

# parse command line args
num_citizens = sys.argv[1]
num_foods = sys.argv[2]
num_jobs = sys.argv[3]

# gather missing input interactively
# TODO: review to see if this logic could be cleaner
if not num_citizens:
    num_citizens = raw_input("Number of citizens: ")
if num_citizens:
    num_citizens = int(num_citizens)
else:
    num_citizens =  random.randint(10,100)

if not num_foods:
    num_foods = raw_input("Number of foods: ")
if num_foods:
    num_foods = int(num_foods)
else:
    num_foods = random.randint(10,100)

if not num_jobs:
    num_jobs = raw_input("Number of jobs: ")
if num_jobs:
    num_jobs = int(num_jobs)
else:
    num_jobs = random.randint(10,100)


# create some food 
foods = []
for x in range(0,num_foods):
    name = "Apple-{}".format(x)
    energy = random.randint(1,6) * 60       # 1-6 hours
    duration = 5 * (24 * 60)                # 5 days

    foods.append(Food.Food(name, energy, duration))

# create some work
jobs = []
for x in range(0,num_jobs):
    name = "Job-{}".format(x)
    duration = 8 * 60                       # 8 hours
    energy = 8 * 60                         # 8 hours worth of energy
    p = 1                                   # this is a physical job
    e = 0
    i = 0
    skills = []                             # not implemented
    tools = []                              # not implemented
    materials = []                          # not implemented
    products = []

    # these jobs emit apples of random energy value 
    product_name = "Product-Apple-{}".format(x)
    product_energy = random.randint(1,6) * 60       # 1-6 hours
    product_duration = 5 * (24 * 60)                # 5 days

    products.append(Food.Food(product_name, product_energy, product_duration))

    jobs.append(Job.Job(name, duration, energy, p, e, i, skills, tools, materials, products))

# create some citizens
citizens = [] 
for x in range(0,num_citizens):
    name = "Charlie-{}".format(x)
    age = random.randint(18,75) * (365 * (24 * 60)) # 18-75 years old
    energy = random.randint(3,5) * (24 * 60)        # 3-5 days worth of energy 

    citizens.append(Citizen.Citizen(name, age, energy))

# start the simulation
print("{} Citizens, {} Pieces of food, {} Jobs".format(len(citizens), len(foods), len(jobs)))
raw_input("Press any enter to begin.")

# loop until they are all toast
dayidx = 1 
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
                # reset last food day
                last_food_day = 0
                
                selected_food = foods.pop()
                print("{} consumed {} (+{}E)".format(citizen.get_name(), selected_food.Name, selected_food.Energy))
                citizen.eat(selected_food)
            else:
                if not last_food_day:
                    last_food_day = dayidx
                    print("Out of food!")

            # work
            if len(jobs) > 0:
                # reset last job day
                last_job_day = 0

		# do the job and add the product to the food bin
                product = citizen.work(jobs.pop())	# 8 hours of work
                if len(product) > 0:
                    print("{} produced {} (+{}E).".format(citizen.get_name(), product[0].Name, product[0].Energy))
                    # TODO: loop throuh and add all food products 
                    foods.append(product[0])
            else:
                citizen.age(60 * 8)         		# 8 hours of idleness
                if not last_job_day:
                    last_job_day = dayidx
                    print("Out of jobs!")

            # leasure
            citizen.age(60 * 8)     # 8 hours of leasure

            # sleep
            citizen.sleep(60 * 8)   # 8 hours of sleep

        else:
            print("{} is dead.".format(citizen.get_name()))
            graveyard.append({"name": citizen.get_name(), "age": citizen.get_age(), "last_day": dayidx});
            citizens.pop(index)

    dayidx = dayidx + 1

print("Community terminated after {} days ({} years). Last day of food: {}, last day of work: {}).".format(dayidx, (dayidx / 365), last_food_day, last_job_day))

print("Citizen Statistics:")
for citizen in graveyard:
    print("{}: age: {} last day: {}".format(citizen["name"], (((citizen["age"]/60)/24)/365), citizen["last_day"]))
