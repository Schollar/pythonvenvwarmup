import dbcreds
import mariadb as db


class dbInteraction:
    # Connect function that starts a DB connection and creates a cursor
    def db_connect(self):
        conn = None
        cursor = None
        try:
            conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                              host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
        except db.OperationalError:
            print('Something is wrong with the DB')
        except:
            print('Something went wrong connecting to the DB')
        return conn, cursor
# Disconnect function that takes in the conn and cursor and attempts to close both

    def db_disconnect(self, conn, cursor):
        try:
            cursor.close()
        except:
            print('Error closing cursor')
        try:
            conn.close()
        except:
            print('Error closing connection')
# User login function. Takes in a username and password, runs a select query to see if any Username and pw in DB match. If they do return true, if not false.

    def user_login(self, username, password):
        user = None
        conn, cursor = self.db_connect()
        try:
            cursor.execute(
                "SELECT * FROM owner WHERE username =? and password =?", [username, password])
            user = cursor.fetchone()
        except db.OperationalError:
            print('Something is wrong with the db!')
        except db.ProgrammingError:
            print('Error running DB query')
        self.db_disconnect(conn, cursor)
        if(user == None):
            print("Invalid username or password!")
            return False
        else:
            print(f'Welcome ', user[1])
            return True

    def show_dogs(self, username):
        dogs = None
        conn, cursor = self.db_connect()
        try:
            cursor.execute(
                "SELECT name, description FROM dog inner join owner on dog.owner = owner.id WHERE username =?", [username, ])
            dogs = cursor.fetchall()
        except db.OperationalError:
            print('Something is wrong with the db!')
        except db.ProgrammingError:
            print('Error running DB query')
        self.db_disconnect(conn, cursor)
        for dog in dogs:
            print(dog[0], ':', dog[1])
