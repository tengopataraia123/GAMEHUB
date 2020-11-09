from flask import Blueprint
from myproject.auth.forms import LoginForm

admin_blueprint = Blueprint("admin",__name__,template_folder="templates/admin")

@admin_blueprint.route("/admin")
def admin():
    pass