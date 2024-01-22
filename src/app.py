from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos ():
    # you can convert that variable into a json string like this
    json_text = jsonify(todos)

    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    json_todo_list= jsonify(todos)
    return json_todo_list

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_todo_list = jsonify(todos)
    return json_todo_list

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)