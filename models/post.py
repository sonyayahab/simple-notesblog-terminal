from database import Database
import uuid
import datetime

# this Post comes from object, we're also treated as a object
class Post(object):

    # default parameters in the end
    #ex: post = Post(blog_id = 123, )
    def __init__(self, blog_id, title, content, author, created_date = datetime.datetime.now(), post_id = None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    def json_dump(self):
        return {
            'id' : self.post_id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json_dump())

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query = {'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]