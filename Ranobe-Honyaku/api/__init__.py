from flask import Blueprint, redirect
from utils import setup_file

API = Blueprint("api", __name__, static_folder="static/api", template_folder="templates/api", url_prefix="/api")


# This is the base for the API; Will redirect to our Github organisation page so it always links to latest documentation
@API.route(rule="")
def root():
    return redirect(setup_file["GITHUB"], 301)