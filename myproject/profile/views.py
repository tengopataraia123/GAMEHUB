from flask import Blueprint,render_template

profile_blueprint = Blueprint("profile",__name__,template_folder="templates/profile")

@profile_blueprint.route("/profile/user=<user_id>")
def profile_view(user_id):
    return render_template("profile.html")