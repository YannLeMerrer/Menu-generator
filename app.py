from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import csv
import sqlite3

from recipe import Recipe

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT,
        image TEXT,
        steps TEXT,
        ingredients TEXT
        )
    ''')


@app.route("/")
def home():
    init_db()
    return render_template('home.html')


@app.route("/recipes", methods=['POST'])
def load_recipes():
    file = request.files['recipes']
    filename = secure_filename(file.filename)
    path = f"/home/pascal/menus/uploads/{filename}"
    file.save(path)
    recipes = []
    with open(path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # Ignore l'en-tête
        for row in csv_reader:
            recipe = create_recipe(row)
            recipes.append(recipe)
    return render_template('recipes.html', recipes=recipes)


def create_recipe(row: list[str]) -> Recipe:
    return Recipe(title=row[0], ingredients=row[6], steps=row[7], image=row[10])
