from flask_restful import Resource,reqparse
from myproject.models import Post

class PostsApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("start",type=int,required=True)
    parser.add_argument("end",type=int,required=True)

    def get(self):
        start = self.parser.parse_args()["start"]
        end = self.parser.parse_args()["end"]
        
        if start < len(Post.query.all()):
            posts = Post.query.order_by(Post.id.desc()).all()[start:end]
        else:
            posts = []
        posts_json = []
        
        for post in posts:
            posts_json.append({
                "id":post.id,
                "title":post.title,
                "text":post.text,
                "date":post.date.strftime("%m/%d/%Y, %H:%M:%S"),
                "reaction":post.reaction,
                "author":post.author.name
            })
        return posts_json