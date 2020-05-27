from cat import *
from doctor import *
from dog import *
from logger import get_cursor
from owner import *


class DataOperator:

    def __init__(self):
        self.cursor, self.mydb = get_cursor()

    # Method that allows us to insert data in database
    def insert_data(self, obj):
        if type(obj) == Pet:
            strD = "INSERT INTO pets (id, name, age, breed, is_castrated,sex, doctor_id, owner_id) VALUES (" \
                   "%s, %s, %s,%s, %s,%s,%s,%s) "
            self.cursor.execute(strD, obj.get_tuple())

        elif type(obj) == Dog:
            strD = "INSERT INTO dogs (id, name, age, breed,is_tail_cut,is_castrated,sound, sex,doctor_id, owner_id) VALUES (" \
                   "%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(strD, obj.get_tuple())
            strD = "INSERT INTO pets (id, name, age, breed, is_castrated,sex, doctor_id, owner_id) VALUES (" \
                   "%s, %s, %s,%s, %s,%s,%s,%s) "
            self.cursor.execute(strD, obj.get_short_tuple())

        elif type(obj) == Cat:
            strD = "INSERT INTO cats (id, name, age, breed, is_castrated,sex, doctor_id, owner_id) VALUES (" \
                   "%s, %s, %s,%s, %s,%s,%s,%s) "
            self.cursor.execute(strD, obj.get_tuple())
            strD = "INSERT INTO pets (id, name, age, breed, is_castrated,sex, doctor_id, owner_id) VALUES (" \
                   "%s, %s, %s,%s, %s,%s,%s,%s) "
            self.cursor.execute(strD, obj.get_tuple())

        elif type(obj)==Person:
            strD = "INSERT INTO persons(id, name, surname, contact) VALUES (%s, %s, %s, %s)"

        elif type(obj)==Doctor:
            strD = "INSERT INTO doctors(id, position,name, surname, contact, salary) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(strD, obj.get_tuple())
            strD = "INSERT INTO persons(id, name, surname, contact) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(strD, obj.get_short_tuple())

        elif type(obj)== Owner:
            strD = "INSERT INTO owners(id, name, surname, contact) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(strD, obj.get_tuple())
            strD = "INSERT INTO persons(id, name, surname, contact) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(strD, obj.get_tuple())

        self.mydb.commit()

    # Method that allows us to drop object with given ID from the database
    def drop_data(self, name_table, id_):
        if name_table=="dogs" or name_table=="cats" or name_table=="Dogs" or name_table=="Cats":
            str1 = "DELETE FROM {} WHERE id = {}".format(name_table, id_)
            str2 = "DELETE FROM Pets WHERE id = {}".format(id_)
        elif name_table=="owners" or name_table=="doctors" or name_table=="Owners" or name_table=="Doctors":
            str1 = "DELETE FROM {} WHERE id = {}".format(name_table, id_)
            str2 = "DELETE FROM Persons WHERE id = {}".format(id_)

        self.cursor.execute(str1)
        self.cursor.execute(str2)
        self.mydb.commit()

    # Method that allows us to update data in given table for any row in it
    def update(self, name_table, id_, dict):
        for key, value in dict.items():
            str = "UPDATE {} SET {} = '{}' WHERE id = {}".format(name_table, key, value, id_)

            self.cursor.execute(str)
            self.mydb.commit()

    # Method that deletes everything from tables Dogs, Cats, Doctors, Owners, Persons, Pets

    def restart_data(self):
        tables = ["dogs", "doctors", "owners", "cats", "persons", "pets"]
        for tab in tables:
            for i in range(1000):
                self.drop_data(tab, i)

    # Method to get last ID from every table, just to not break the program trying to add primary key that was
    # already used

    def get_last_id(self):

        self.cursor.execute("select id from Pets order by id desc limit 1")
        last_id_pet = self.cursor.fetchone()
        if last_id_pet != None:
            Pet.class_counter = last_id_pet[0]

        self.cursor.execute("select id from Persons order by id desc limit 1")
        last_id_person = self.cursor.fetchone()
        if last_id_person!=None:
            Person.class_counter = last_id_person[0]

    # Method returns  data from given table and row with ID
    def get_data(self, table_name, id):
        try:
            str = "SELECT * FROM {} WHERE id={}".format(table_name, id)
            self.cursor.execute(str)
            return self.cursor.fetchall()[0]
        except IndexError:
            print("Table is empty")

    # Method that returns the whole data from the table
    def get_data_base(self, table_name):
        str1 = "SELECT * FROM {}".format(table_name)
        self.cursor.execute(str1)
        return self.cursor.fetchall()

    # Method that returns list of ID's of given table
    def get_id_data_base(self, table_name):
        str1 = "SELECT id FROM {}".format(table_name)
        self.cursor.execute(str1)
        return self.cursor.fetchall()



