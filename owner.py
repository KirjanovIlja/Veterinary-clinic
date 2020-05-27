from person import *


# Child class Owner inherits from class Person

class Owner(Person):

    def __init__(self):
        super().__init__()

    def get_info(self):
        return "{}. {} {} {} ".format(self.get_id(), self.get_name(), self.get_surname(), self.get_contact())