from flask import Flask, jsonify, request
import get_prediction from control.py 

app=Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'a',
        'done': False
    },
    {
        'id': 2,
        'title': u'b',
        'done': False
    },
        {
        'id': 3,
        'title': u'c',
        'done': False
    },
    {
        'id': 4,
        'title': u'd',
        'done': False
    },
    {
        'id': 5,
        'title': u'e',
        'done': False
    },
    {
        'id': 6,
        'title': u'f',
        'done': False
    },
    {
        'id': 7,
        'title': u'g',
        'done': False
    },
    {
        'id': 8,
        'title': u'h',
        'done': False
    },
    {
        'id': 9,
        'title': u'i',
        'done': False
    },
    {
        'id': 10,
        'title': u'j',
        'done': False
    },
    {
        'id': 11,
        'title': u'k',
        'done': False
    },
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)