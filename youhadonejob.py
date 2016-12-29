import Citizen
import Job

# create a citizen (21 years old, 5 days of energy)
joe = Citizen.Citizen("Joe", (18 * (365 * (24 * 60))), (5 * (24 * 60)))

print("Before")
joe.print_status()

# create a physical job (1 day long, 1 day of physical energy)
shovel_coal = Job.Job("Shovel coal", (8 * 60), (8 * 60), 0, 1, 0, ["shoveling"], None, ["shovel"], None);

print("After")
# execute job 5 times
for x in range(0,5):
    joe.work(shovel_coal)
    joe.age(16 * 60)
    joe.print_status()
