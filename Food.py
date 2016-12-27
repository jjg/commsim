class Food(object):
    
    def __init__(self, name, energy, duration):
        self.Name = name
        self.Energy = energy
        self.Duration = duration

    def age(self, minutes):
        self.Duration = self.Duration - minutes
