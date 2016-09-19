from flask import Flask

from api import API
from utils import setup_file


app = Flask(__name__)

# All of our config stuff
app.secret_key = setup_file["SECRET_KEY"]

# Registering the applications blueprints
app.register_blueprint(API)

app.run(host="localhost", port=5000, debug=True)
