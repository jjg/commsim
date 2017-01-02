import math
import decimal
from datetime import datetime
import string
import Termcolor
import Citizen_Status

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
        self.current_activity_name = ""
        self.current_activity_remain = 0

    # destructor
    def __del__(self):
        # TODO: tear-down the citizen
        pass

    # public methods
    def get_status(self):
        status = Citizen_Status.Citizen_Status()

        if self.__PE < 10:
            status.hungry = True
        if self.__EE < 10:
            status.depressed = True
        if self.__IE < 10:
            status.tired = True
        if len(self.Activity) < 1:
            status.idle = True

        # TODO: add high-range status thresholds 

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
        self.Activity.append(activity)

    def age(self, minutes):

        # increment age
        self.__Age = self.__Age + minutes

        # subtract 1 (modified) PE unit just to keep the body warm
        self.__PE = self.__PE - (minutes * (-self.physical() * 1))

        # apply additional internal state modifications based on activity
        if len(self.Activity) > 0 :

            # apply current activity to citizen's internal state
            current_activity = self.Activity.pop()
            self.current_activity_name = current_activity.Name

            # TODO: further modify this based on skill level
            self.__PE = self.__PE - (minutes * (-self.physical() * current_activity.Physical))
            self.__EE = self.__EE - (minutes * (-self.emotional() * current_activity.Emotional))
            self.__IE = self.__IE - (minutes * (-self.intellectual() * current_activity.Intellectual))

            # TODO: increse skill levels based on skills associated with job
            # (inc. skill +1 each time a skill is used)

            # decrement activity duration
            current_activity.Duration = current_activity.Duration - minutes
            self.current_activity_remain = current_activity.Duration

            # if activity isn't complete, put it back on the pile
            if current_activity.Duration > 0:
                self.Activity.append(current_activity)
            else:
                # emit any products of the activity
                return current_activity.Products

        else:
            # reset current activity trackers
            self.current_activity_name = "idle"
            self.current_activity_remain = 0

        # TODO: When a single PEI state reaches certain thresholds it can impact others
        # i.e., when P is too low it should cause E to drop, etc.

    def physical(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 23.0))

    def emotional(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 28.0))

    def intellectual(self):
        return math.sin((((2.0 * math.pi) * (self.__Age / 525600.0)) / 33.0))

    def print_status(self):
        print("{1}{3}\t{0}Age: {1}{4}\t {0}P: {1}{5:n}{2}\t{0}E: {1}{6:n}{2}\t{0}I: {1}{7:n}{2}\t{0}A: {1}{8}({9}){2}".format(
            Termcolor.colors.HEADER,
            Termcolor.colors.OKGREEN,
            Termcolor.colors.ENDC,
            self.__Name, 
            (((self.__Age / 60) / 24) / 365), 
            self.__PE,
            self.__EE,
            self.__IE,
            self.current_activity_name,
            self.current_activity_remain))
