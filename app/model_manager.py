from flask import jsonify, request
from flask_restful import Resource
import uuid


class ModelManager(Resource):
    """A class to manage uploading and downloading models, these models could be already trained
    or they could be a brand new model."""

    def __init__(self):
        self.model_url = "models:/travisa/travis_awesome_model/1.0/travis_encoder"
        self.model_description = "This is Travis's initial model"
        self.model_version = 1.0
        self.model_id = uuid.uuid4()

    def get(self, model_url):
        return jsonify({'model_id': self.model_id},{'model_description': self.model_description},{'model_url': model_url})

    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201