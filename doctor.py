from person import *


# Child class Doctor inherits from class Person
class Doctor(Person):

    def __init__(self):
        super().__init__()
        self._position = ""
        self._salary = 0

    def set_position(self, pos):
        self._position = pos

    def set_salary(self, sal):
        self._salary = sal

    def get_salary(self):
        return self._salary

    def get_position(self):
        return self._position

    def get_info(self):
        return "{}. {} {} {} {}".format(self.get_id(), self.get_position(), self.get_name(), self.get_surname(), self.get_contact())

    def get_tuple(self):
        return (self.get_id(),
                self.get_position(),
                self.get_name(),
                self.get_surname(),
                self.get_contact(),
                self.get_salary()
                )

    def get_short_tuple(self):
        return(self.get_id(),
               self.get_name(),
               self.get_surname(),
               self.get_contact())