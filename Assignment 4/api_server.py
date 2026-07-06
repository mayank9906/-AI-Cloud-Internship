from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():
    with open("students.json", "r", encoding="utf-8") as file:
        students = json.load(file)

    return jsonify(students)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)