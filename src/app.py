from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "My third task", "done": False },
    { "label": "My fourth task", "done": False },
    { "label": "My fifth task", "done": False },
    { "label": "My sixth task", "done": False },
    { "label": "My seventh task", "done": False },
    { "label": "My eighth task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
   return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)