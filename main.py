from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gamebase.db'
db = SQLAlchemy(app)

class GameModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    platform = db.Column(db.String(200), nullable=False)
    score = db.Column(db.String(10), nullable=False)
    genre = db.Column(db.String(200), nullable=False)
    editors_choice = db.Column(db.String(1), nullable=False)
    def __repr__(self):
        return f"Game(title = {title}, platform = {platform}, score = {score}, genre = {genre}, editors_choice = {editors_choice})"

db.create_all()

game_post_args = reqparse.RequestParser()
game_post_args.add_argument("title", type=str, help="Title of the game is required", required=True)
game_post_args.add_argument("platform", type=str, help="Platform of the game is required", required=True)
game_post_args.add_argument("score", type=int, help="Score of the game is required", required=True)
game_post_args.add_argument("genre", type=str, help="Genre of the game is required", required=True)
game_post_args.add_argument("editors_choice", type=str, help="Editors_choice of the game is required", required=True)

game_update_args = reqparse.RequestParser()
game_update_args.add_argument("title", type=str, help="Title of the game is required", required=True)
game_update_args.add_argument("platform", type=str, help="Platform of the game is required", required=True)
game_update_args.add_argument("score", type=int, help="Score of the game is required", required=True)
game_update_args.add_argument("genre", type=str, help="Genre of the game is required", required=True)
game_update_args.add_argument("editors_choice", type=str, help="Editors_choice of the game is required", required=True)

resource_fields = {
	'title': fields.String,
	'platform': fields.String,
	'score': fields.Integer,
	'genre': fields.String,
    'editors_choice': fields.String
}
class Game(Resource):
    def __init__(self):
        pass

    @marshal_with(resource_fields)
    def get(self, game_id):
        result = GameModel.query.filter_by(id=game_id).first()
        if not result:
            abort(404, message="Could not find game with that title")
        return result

    @marshal_with(resource_fields)
    def post(self, name, cls):
        args = game_post_args.parse_args()
        game = GameModel(title= args['title'],
                   platform= args['platform'],
                   score= args['score'],
                   genre= args['genre'],
                   editors_choice= args['editors_choice'])
        db.session.add(game)
        db.session.commit()

        return game, 201

        @marshal_with(resource_fields)
	    def put(self, game_id):
            args = game_put_args.parse_args()
            result = GameModel.query.filter_by(id=game_id).first()
            if result:
                abort(409, message="Game id taken...")

            game = GameModel(id=game_id, title= args['title'],
                    platform= args['platform'],
                    score= args['score'],
                    genre= args['genre'],
                    editors_choice= args['editors_choice'])

            db.session.add(game)
            db.session.commit()
            return video, 201

        @marshal_with(resource_fields)
	    def patch(self, game_id):
            args = game_update_args.parse_args()
            result = GameModel.query.filter_by(id=game_id).first()
            if not result:
                abort(404, message="game doesn't exist, cannot update")

            if args['title']:
                result.name = args['title']
            if args['platform']:
                result.views = args['platform']
            if args['score']:
                result.likes = args['score']
            if args['genre']:
                result.views = args['genre']
            if args['editors_choice']:
                result.likes = args['editors_choice']

            db.session.commit()

            return result

        def delete(self, game_id):
		abort_if_game_id_doesnt_exist(game_id)
		del Game[game_id]
		return '', 204

api.add_resource(Game,'/game//<int:game_id>')
api.add_resource(Game,'/game/<int:game_id>')
if __name__ == "__main__":
	app.run(debug=True)

