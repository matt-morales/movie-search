import click
from flask import jsonify, Flask

#  from es import  es_client


app = None


def create_app(testing=False):
    global app

    app = Flask(__name__)


    @app.route("/test")
    def test():
        return jsonify({"success": True}), 200


    @app.cli.command("load-movielens")
    def load_movielens():
        return jsonify({"success": True}), 200

    return app
