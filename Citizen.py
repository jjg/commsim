import math
import decimal
from datetime import datetime
import string
import Termcolor

class Citizen(object):

    # constructor
    def __init__(self, name, age, pe, ee, ie):
        self.__Name = name
        self.__Age = age 
        self.__PE = float(pe)
        self.__EE = float(ee)
        self.__IE = float(ie)
        self.Skills = []
        self.Activity = []

    # destructor
    def __del__(self):
        # TODO: tear-down the citizen
        pass

    # public methods
    def get_status(self):
        status = {}
        status.hungry = False
        status.depressed = False
        status.tired = False
        status.idle = False

        if self.__PE < 1:
            status.hungry = True
        if self.__EE < 1:
            status.depressed = True
        if self.__IE < 1:
            status.tired = True
        if len(self.__Activity) < 1:
            status.idle = True

        return status

    def get_name(self):
        return self.__Name

    def get_age(self):
        return self.__Age

    def get_PE(self):
        return self.__PE

    def get_EE(self):
        return self.__EE

    def get_IE(self):
        return self.__IE

    def add_activity(self, activity):
        self.__Activity.append(activity)

    def age(self, minutes):

        # increment age
        self.__Age = self.__Age + minutes

        # if no activity, just subtract 1 from PE
        if len(self.Activity) < 1:
            self.__PE = self.__PE - minutes
        else :
            # apply top activity to citizen's internal state
            current_activity = self.__Activity.pop()

            # TODO: further modify this based on skill level
            self.__PE = self._PE - (minutes * (-self.physical() * current_activity.Physical))
            self.__EE = self._PE - (minutes * (-self.emotional() * current_activity.Emotional))
            self.__IE = self._IE - (minutes * (-self.intellectual() * current_activity.Intellectual))

            # TODO: increse skill levels based on skills associated with job
            # (inc. skill +1 each time a skill is used)

            # decrement activity duration
            current_activity.Duration = current_activity.Duration - minutes

            # if activity isn't complete, put it back on the pile
            if current_activity.Duration > 0:
                self.__Activity.append(current_activity)
            else:
                # emit any products of the activity
                return current_activity.Products

            # ORIGINAL JOB ENERGY CONSUMPTION MATH
            #self.__Energy = self.__Energy - \
            #    (job.Energy * (-self.physical() * job.Physical)) - \
            #    (job.Energy * (-self.emotional() * job.Emotional)) - \
            #    (job.Energy * (-self.intellectual() * job.Intellectual))

    def physical(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 23.0))

    def emotional(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 28.0))

    def intellectual(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 33.0))

    def print_status(self):
        print("{1}{3}\t{0}P: {1}{4:.2%}\t{0}E: {1}{5:.2%}\t{0}I: {1}{6:.2%}\t{0}Age: {1}{7}\t {0}P: {1}{8:n}{2}\t{0}E: {1}{9:n}{2}\t{0}I: {1}{10:n}{2}".format(
            Termcolor.colors.HEADER,
            Termcolor.colors.OKGREEN,
            Termcolor.colors.ENDC,
            self.__Name, 
            self.physical(),
            self.emotional(),
            self.intellectual(), 
            (((self.__Age / 60) / 24) / 365), 
            self.__PE,
            self.__EE,
            self.__IE))
