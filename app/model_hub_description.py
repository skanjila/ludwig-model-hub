from flask import jsonify, request
from flask_restful import Resource
"""A class off the root of the basepath that returns metadata for now about the ludwig model hub"""


class ModelHubDescription(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return jsonify({'message': 'Welcome to the ludwig model hub'})


