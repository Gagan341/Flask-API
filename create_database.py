from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gamebase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

cereal_df = pd.read_csv("games_data.csv")


class GameModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    platform = db.Column(db.String(200))
    score = db.Column(db.String(10))
    genre = db.Column(db.String(200))
    editors_choice = db.Column(db.String(1))
    def __repr__(self):
        return f"Game(id = {id}, title = {title}, platform = {platform}, score = {score}, genre = {genre}, editors_choice = {editors_choice})"
# Uncomment once to create database 
# db.create_all()

for x in range(len(cereal_df['title'])):
    game = GameModel(id= x,
                    title= str(cereal_df['title'][x]),
                    platform= str(cereal_df['platform'][x]),
                    score= str(cereal_df['score'][x]),
                    genre= str(cereal_df['genre'][x]),
                    editors_choice= str(cereal_df['editors_choice'][x]))

    db.session.add(game)
    db.session.commit()

result = GameModel.query.filter_by(title = 'Fable: The Journey').first()
print(result)
if __name__ == "__main__":
	app.run(debug=True)