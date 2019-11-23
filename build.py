#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from sqlalchemy import create_engine
# from json import dumps

app = Flask(__name__)
api = Api(app)

birth_data = {}
class Birthyear(Resource):
    def get(self, user):
        return {user: birth_data[user]}

    def post(self, user):
        birth_data[user] = request.form['data']
        return{user: birth_data[user]}

    def delete(self, user):
        del birth_data[user]
        return birth_data
        
class Showall(Resource):
    def get(self):
        return birth_data

api.add_resource(Birthyear, '/<string:user>')
api.add_resource(Showall, '/')

if __name__ == '__main__':
     app.run(debug=True)