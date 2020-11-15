from flask import Blueprint,redirect,url_for
from flask_login import current_user
from myproject.models import Post
from myproject import db

post_blueprint = Blueprint("post",__name__,template_folder="templates/post")

@post_blueprint.route("/deletepost/<int:postId>")
def detelePost(postId):
    post = Post.query.get(postId)

    if current_user.id == post.author.id:
        db.session.delete(post)
        db.session.commit()
    
    return redirect(url_for("index.index"))