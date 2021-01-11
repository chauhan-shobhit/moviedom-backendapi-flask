from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db


from resources.user import UserResource
from resources.movie import MovieCatalogResource, MovieResource

def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)

    api = Api(app)
    api.add_resource(MovieCatalogResource, '/movies')
    api.add_resource(MovieResource,'/movies/<int:movie_id>' )
    api.add_resource(UserResource, '/register')

    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

if __name__ =='__main__':
    app = init_app()
    app.run(port=Config.APPLICATION_PORT, debug=True)