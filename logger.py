import mysql.connector


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


#@run_once
def get_cursor():
    mydb = mysql.connector.connect(host="127.0.0.1",
                                   user="root",
                                   passwd="Kirjanov77!mysql",
                                   auth_plugin="mysql_native_password",
                                   port="3306",
                                   database="veterinary_clinic")
    cursor = mydb.cursor()
    return cursor, mydb










    '''
        try:
            self.cursor.execute("CREATE DATABASE VeterinaryClinic")
        except mysql.connector.errors.DatabaseError:
            pass

        tables = ["CREATE TABLE Pets", "CREATE TABLE STAFF"]

        for table in tables:
            try:
                self.cursor.execute(table)
            except mysql.connector.errors.ProgrammingError:
                pass
    '''


