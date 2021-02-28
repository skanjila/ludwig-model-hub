import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db


@application.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the APIs for the Ludwig model hub!'
    )


@application.route('/ludwig_model_hub/models/metadata')
def get_model_metadata():
    _models = db.model.find()

    item = {}
    data = []
    for model in _models:
        item = {
            'url': str(model['model_url']),
            'id': str(model['model_id']),
            'description': str(model['model_description']),
            'version': str(model['model_version']),
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )


@application.route('/ludwig_model_hub/upload', methods=['POST'])
def create_model():
    data = request.get_json(force=True)
    item = {
        'model': data['model']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 8080)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
