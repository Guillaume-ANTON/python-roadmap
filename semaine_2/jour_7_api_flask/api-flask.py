from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

tasks = []

class TaskList(Resource):
    def get(self):
        return {'tasks': tasks}, 200
    
    def post(self):
        data = request.get_json()
        task = {'id': len(tasks) + 1, 'title': data['title'], 'done': False}
        tasks.append(task)
        return task, 201

class Task(Resource):
    def get(self, task_id):
        task = next((t for t in tasks if t['id'] == task_id), None)
        if task:
            return task, 200
        return {'message': 'Task not found'}, 404
    
    def put(self, task_id):
        task = next((t for t in tasks if t['id'] == task_id), None)
        if task:
            data = request.get_json()
            task.update({'title': data.get('title', task['title']), 'done': data.get('done', task['done'])})
            return task, 200
        return {'message': 'Task not found'}, 404
    
    def delete(self, task_id):
        global tasks
        tasks = [t for t in tasks if t['id'] != task_id]
        return {'message': 'Task deleted'}, 200

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
