from flask import Blueprint,render_template
from myproject.models import Gamer
from myproject import active_users

profile_blueprint = Blueprint("profile",__name__,template_folder="templates/profile")

@profile_blueprint.route("/profile/<user_id>")
def profile_view(user_id):
    global active_users
    user = Gamer.query.get(user_id)
    active = False

    if user_id in active_users:
        active = True
    print(active)
    return render_template("profile.html",user=user,active=active)