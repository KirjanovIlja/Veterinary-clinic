from pet import *


# Child class Dog inherits from class Pet

class Dog(Pet):

    def __init__(self):
        super().__init__()
        self._sound = "Wooof"
        self._is_tail_cut = "No"

    def get_sound(self):
        return self._sound

    def set_sound(self, sound):
        self._sound = sound

    def get_is_tail_cut(self):
        return self._is_tail_cut

    def set_is_tail_cut(self, tail):
        self._is_tail_cut = tail

    def get_info(self):
        return "{}. {} {} doggo {} {} {}".format(self.get_id(), self.get_breed(), self.get_age(), self.get_name(), self.get_doctor_id(), self.get_owner_id())

    def get_tuple(self):
        return (self.get_id(),
                self.get_name(),
                self.get_age(),
                self.get_breed(),
                self.get_is_tail_cut(),
                self.get_castrated(),
                self.get_sound(),
                self.get_sex(),
                self.get_doctor_id(),
                self.get_owner_id())

    def get_short_tuple(self):
        return (self.get_id(),
                self.get_name(),
                self.get_age(),
                self.get_breed(),
                self._castrated,
                self.get_sex(),
                self.get_doctor_id(),
                self.get_owner_id())
