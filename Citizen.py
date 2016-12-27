import math
import decimal
from datetime import datetime
import string
import Termcolor

class Citizen(object):

    # constructor
    def __init__(self, name, age, energy):
        self.__Name = name
        self.__Age = age 
        self.__Energy = energy
        self.Skills = [] 

    # destructor
    def __del__(self):
        #TODO: tear-down the citizen
        pass

    # public methods
    def get_name(self):
        return self.__Name

    def get_energy(self):
        return self.__Energy

    def eat(self, food):
        self.__Age = self.__Age + 1
        self.__Energy = self.__Energy + food.Energy

    def sleep(self, minutes):
        self.__Age = self.__Age + minutes
        self.__Energy = self.__Energy + minutes

    def work(self, job):
        self.__Age = self.__Age + job.Duration
        self.__Energy = self.__Energy - job.Energy
        #TODO: increse skill levels based on skills associated with job
        # (inc. skill +1 each time a skill is used)

    def age(self, minutes):
        # update the citizen's internal state to reflect specified minutes of aging
        #TODO: other faactors will eventually impact change rates, for now just simple inc/dec 
        self.__Age = self.__Age + minutes
        self.__Energy = self.__Energy - minutes 

    def physical(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 23.0))

    def emotional(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 28.0))

    def intellectual(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 33.0))

    def print_status(self):
        print("{1}{3}\t{0}P: {1}{4:.2%}\t{0}E: {1}{5:.2%}\t{0}I: {1}{6:.2%}\t{0}Age: {1}{7}\t {0}Energy: {1}{8}{2}".format(
            Termcolor.colors.HEADER,
            Termcolor.colors.OKGREEN,
            Termcolor.colors.ENDC,
            self.__Name, 
            self.physical(),
            self.emotional(),
            self.intellectual(), 
            (((self.__Age / 60) / 24) / 365), 
            self.__Energy))
