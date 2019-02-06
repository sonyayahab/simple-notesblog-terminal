from models.post import Post
from database import Database

database = Database.initialize()

post = Post(1,
            "Hellow World",
            "This is the second content",
            "Sony Wicaksono")

post.save_to_mongo()
posts = post.from_blog(1)

for post in posts:
    print (post)
