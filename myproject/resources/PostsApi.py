from flask_restful import Resource,reqparse
from myproject.models import Post

class PostsApi(Resource):
    parser = reqparse.RequestParser()
    index = 0
    parser.add_argument("count",type=int,required=True)

    def get(self):
        count = self.parser.parse_args()["count"]
        posts = Post.query.order_by(Post.id.desc()).all()[self.index:self.index+count]

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

        self.index += count
        return posts_json