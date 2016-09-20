from flask import Flask, render_template

from api import API
from admin import admin
from utils import setup_file


app = Flask(__name__)

# All of our config stuff
app.secret_key = setup_file["SECRET_KEY"]

# Registering the applications blueprints
app.register_blueprint(API)
app.register_blueprint(admin)


@app.route(rule="/")
def home():
    return render_template("home.html", setup_file=setup_file)

# Run our dev server; Remove once app is in production setting!
app.run(host="localhost", port=5000, debug=True)
