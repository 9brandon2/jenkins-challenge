#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
birth_data = {}
class Birthyear(Resource):
    def __init__(self, birth_data=birth_data):
        self.birth_data = birth_data

    def get(self, user):
        print (user)
        if user in list(self.birth_data.keys()):
            return {user: self.birth_data[user]}, 200
        else:
            return 404

    def post(self, user):
        try:
            data = int(request.form['data'])
        except ValueError:
            return 403
        self.birth_data[user] = data
        print("length..:", data.bit_length())
        if data.bit_length() > 32:
            return "Incorrect Value Size", 400
        else:
            print ({user: self.birth_data[user]})
            return {user: self.birth_data[user]}, 204

    def delete(self, user):
        if user in list(self.birth_data.keys()):
            del self.birth_data[user]
            return self.birth_data, 204
        else:
            return 400
        
# class Showall(Resource):
#     def __init__(self, birth_data={}):
#         self.birth_data = birth_data

#     def get(self):
#         return self.birth_data

api.add_resource(Birthyear, '/<string:user>')
# api.add_resource(Showall, '/')

if __name__ == '__main__':
     app.run(debug=True)
