import dbhandler as dbh
import getpass as gp

db = dbh.dbInteraction()

print('Welcome to the Pet Inventory!')
print('Please Login to continue')
username = input('Username: ')
password = gp.getpass('Password: ')

if(db.user_login(username, password)):
    db.show_dogs(username)
else:
    exit()
