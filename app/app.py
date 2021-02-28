# using flask_restful
from flask import Flask
from flask_restful import Api
from model_manager import ModelManager
from model_hub_description import ModelHubDescription


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

api.add_resource(ModelHubDescription, '/')
api.add_resource(ModelManager, '/ludwig_model_hub/<string:model_url>')

# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
