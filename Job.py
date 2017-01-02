class Job(object):

    def __init__(self, name, duration, energy, p, e, i, skills, materials, tools, products):
        self.Name = name
        self.Duration = duration
        self.Skills = skills
        self.Tools = tools
        self.Materials = materials
        self.Products = products

        # biorhythm properties
        self.Physical = p
        self.Emotional = e
        self.Intellectual = i
