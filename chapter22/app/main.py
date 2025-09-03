from models.models import create_tables
from services.services import create_user,create_post,get_user_by_id,get_post_by_id,get_posts_by_user

create_tables()

# Create or Insert data
# result = create_user("vicky","vicky@example.com")
#create_user("nisha","nisha@example.com")
# print(result)

# create_post(1,"Fastapi dev Journey","This is 51th lecture of Fastapi",11)
#create_post(3,"AIML Journey","This is 51th lecture of AIML",11)
#create_post(4,"Blockchain Journey","This is 51th lecture of AIML",1)
#create_post(5,"langchain Journey","This is 51th lecture of AIML",1)

#print(get_post_by_id(1))

print(get_posts_by_user(1))