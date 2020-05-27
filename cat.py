from pet import *


# Child class Cat inherits from class Pet
class Cat(Pet):

    def __init__(self):
        super().__init__()

    def get_info(self):
        return "{}. {} {} cat {}".format(self.get_id(), self.get_breed(), self.get_age(), self.get_name())

