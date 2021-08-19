# flask_web/app.py
import json

from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api
import requests
from config import Config

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


api = Api(app)

todos = {}


class Todo(Resource):
    def get(self, todo_id):
        with open("todos.json", "r") as file:
            try:
                all_data = json.load(file)
                for item in all_data:
                    if item == str(todo_id):
                        data = {todo_id: todos[todo_id]}
                return data
            except KeyError:
                return Response("Not found", status=404)

    def put(self, todo_id):
        data = {todo_id: request.json.get("text")}
        with open("todos.json", "r") as file:
            all_data = json.load(file)
            for item in all_data:
                if item == str(todo_id):
                    all_data[item] = request.json.get("text")
        with open("todos.json", "w") as file:
            json.dump(all_data, file)
        return data

    def delete(self, todo_id):
        with open(f"todos.json", "r") as file:
            all_data = json.load(file)
            for item in list(all_data):
                if item == str(todo_id):
                    del all_data[item]
        with open(f"todos.json", "w") as file:
            json.dump(all_data, file)
        return Response(todos, status=204)


class TodoList(Resource):

    def get(self):
        with open("todos.json", "w") as file:
            json.dump(todos, file)
        return todos

    def post(self):
        todos[request.json.get("todo_id", None)] = request.json.get("text", "")
        with open("todos.json", "w") as file:
            json.dump(todos, file)
        return todos


class Weather(Resource):
    def get(self):
        weather = []
        cities_list = request.args.get("city")
        cities = cities_list.split(",")
        for city in cities:
            querystring = {"q": city, "cnt": 1, "mode": "null", "lon": "", "type": "link, accurate", "lat": "",
                           "units": "imperial, metric"}

            headers = {
                "x-rapidapi-key": Config.WEATHER_API_KEY,
                "x-rapidapi-host": Config.WEATHER_API_HOST
            }

            response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
            if response.status_code == 200:
                data = response.json()
                weather.append(data["list"])
            else:
                return Response(status=404)
        return weather


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")
api.add_resource(Weather, "/weather")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
