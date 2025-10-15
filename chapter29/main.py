from services.services import create_user,create_owner
from db.db import create_tables

#create_tables()

#create_user("vicky","vicky@example.com")

new_owner = create_owner("bunny", "bunny@example.com")
print(new_owner)