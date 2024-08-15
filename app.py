from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/recipes", methods=['POST'])
def create_recipe():
    file = request.files['recipes']
    filename = secure_filename(file.filename)
    path = f"/home/pascal/menus/uploads/{filename}"
    file.save(path)
    with open(path, "r") as f:
        print(f.readlines())
    return "<p>Recettes reçues</p>"