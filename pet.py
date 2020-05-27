class Pet:
    class_counter = 0

    def __init__(self):
        self._name = ""
        self._age = ""
        self._breed = ""
        self._sex = ""
        self._castrated = "No"
        self._doctor_id = -1
        self._owner_id = -1
        self._id = Pet.class_counter+1
        Pet.class_counter +=1

    def set_doctor_id(self, id):
        self._doctor_id = id

    def set_owner_id(self, id):
        self._owner_id = id

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_breed(self, breed):
        self._breed = breed

    def set_castrated(self, cast):
        self._castrated = cast

    def get_castrated(self):
        return self._castrated

    def set_sex(self, s):
        self._sex = s

    def get_doctor_id(self):
        return self._doctor_id

    def get_owner_id(self):
        return self._owner_id

    def get_sex(self):
        return self._sex

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_breed(self):
        return self._breed

    def get_id(self):
        return self._id

    def get_tuple(self):
        return (self.get_id(),
                self.get_name(),
                self.get_age(),
                self.get_breed(),
                self._castrated,
                self.get_sex(),
                self.get_doctor_id(),
                self.get_owner_id())

    @staticmethod
    def get_class_details():
        print("This is Pet class")