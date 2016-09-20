from flask import Blueprint, url_for, render_template

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("")
def dashboard():
    return render_template("admin/dashboard.html")
