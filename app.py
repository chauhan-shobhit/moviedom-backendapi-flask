from flask import Flask
from flask_restful import Api   

from resources.movie import MovieCatalogResource

app = Flask(__name__)

api = Api(app)

api.add_resource(MovieCatalogResource, '/movies')

if __name__ =='__main__':
    app.run(port=8000, debug=True)