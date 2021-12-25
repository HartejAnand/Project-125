from flask import Flask, jsonify, request
import get_prediction from control.py 

app=Flask(__name__)


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

if (__name__ == "__main__"):
    app.run(debug=True)
