class Job(object):

    def __init__(self, name, duration, energy, skills, materials, tools, products):
        self.Name = name
        self.Duration = duration
        self.Energy = energy
        self.Skills = skills
        self.Tools = tools
        self.Materials = materials
        self.Products = products

        # TODO: include biorhythm properties 
