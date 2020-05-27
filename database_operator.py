import mysql.connector

from logger import *


class DataBaseOperator:

    def __init__(self):
        self.cursor, self.mydb = get_cursor()

    # Method to add new column with given column name and data type to given table
    def add_column(self, name_table, column_name, data_type):
        add_str = "ALTER TABLE {} ADD COLUMN {} {} NOT NULL".format(name_table, column_name, data_type)
        try:
            self.cursor.execute(add_str)
        except mysql.connector.errors.ProgrammingError:
            pass

    # Method to drop column by given name from given table
    def drop_column(self, name_table, column_name):
        drop_str = "ALTER TABLE {} DROP COLUMN {}".format(name_table, column_name)
        try:
            self.cursor.execute(drop_str)
        except :
            pass

    # Start method necessary to add tables for the program
    # Can be easily changed for any purpose and sense of program

    def add_tables(self):
        self.cursor.execute("create table if not exists Owners(id int not null,  name varchar(30), surname varchar("
                            "30), contact varchar (30), primary key (id))")

        self.cursor.execute("create table if not exists Persons(id int not null,  name varchar(30), surname varchar("
                            "30), contact varchar (30), primary key (id))")

        self.cursor.execute("create table if not exists Doctors(id int not null, position varchar(30), salary int, "
                            "name varchar(30), surname varchar(30), contact varchar (30), primary key (id))")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Pets(id int not null, name varchar(30), age int, "
                            "breed varchar(30), is_castrated varchar(3),sex varchar(1), doctor_id int, owner_id int, "
                            "primary key (id), foreign key (owner_id) references owners(id) ON UPDATE CASCADE ON "
                            "DELETE CASCADE, foreign key (doctor_id) references doctors(id) ON UPDATE CASCADE ON "
                            "DELETE CASCADE) ")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Cats(id int not null, name varchar(30), age int, "
                            "breed varchar(30), is_castrated varchar(3),sex varchar(1), doctor_id int, owner_id int, "
                            "primary key (id), foreign key (owner_id) references owners(id) ON UPDATE CASCADE ON "
                            "DELETE CASCADE, foreign key (doctor_id) references doctors(id) ON UPDATE CASCADE ON "
                            "DELETE CASCADE) ")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Dogs(id int not null, name varchar(30), age int, "
                            "breed varchar(30), is_castrated varchar(3), sex varchar(1), is_tail_cut varchar(3), "
                            "sound varchar(30), doctor_id int, owner_id int, "
                            "primary key (id), foreign key (owner_id) references owners(id) ON UPDATE CASCADE ON "
                            "DELETE CASCADE, foreign key (doctor_id) references doctors(id) ON UPDATE CASCADE ON "
                            "DELETE CASCADE)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Pet_hotel (id_place int not null, id_pet int, date_start "
                            "varchar(20), "
                            "date_finish varchar(20),duration int, days_remain int, price int, primary key ("
                            "id_place), foreign key (id_pet) references pets(id) on update cascade on delete cascade)")

    # Method to drop table
    def drop_table(self, table_name):
        str = "DROP TABLE {}".format(table_name)
        self.cursor.execute(str)










