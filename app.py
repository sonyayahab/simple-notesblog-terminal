from models.post import Post
from database import Database

database = Database.initialize()

post = Post(1,
            "Hellow World",
            "This is the second content",
            "Sony Wicaksono")

# It will save the post into the mongo database
post.save_to_mongo()

# It will print out into the terminal about the post that have blog_id = 1
posts = post.from_blog(1)
for post in posts:
    print (post)

# It will print out into terminal which post that have id
postid = post.from_mongo("5c5af7ee2f5ac2381a1bea53")
