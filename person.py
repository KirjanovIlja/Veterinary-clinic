class Person:
    class_counter = 0

    def __init__(self):
        self._name = ""
        self._surname = ""
        self._contact = 0
        self._id = Person.class_counter+1
        Person.class_counter += 1

    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    def set_contact(self, contact):
        self._contact = contact

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_contact(self):
        return self._contact

    def get_id(self):
        return self._id

    def get_tuple(self):
        return(self.get_id(),
               self.get_name(),
               self.get_surname(),
               self.get_contact())
