from flask import Blueprint,render_template,redirect,url_for
from myproject.models import Gamer
from myproject import active_users
from myproject.profile.forms import UploadForm
from werkzeug.utils import secure_filename
from myproject.models import Photo

profile_blueprint = Blueprint("profile",__name__,template_folder="templates/profile")

@profile_blueprint.route("/profile/<user_id>",methods=["GET","POST"])
def profile_view(user_id):
    global active_users
    user = Gamer.query.get(user_id)

    if not user:
        return redirect(url_for("index.index"))

    active = False

    form = UploadForm()

    if int(user_id) in active_users:
        active = True

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('static/uploads/'+filename)
        newPhoto = Photo('uploads/'+filename,user_id)

    return render_template("profile.html",user=user,active=active,form=form)