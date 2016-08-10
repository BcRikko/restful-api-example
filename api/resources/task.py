import os
import json
import falcon

class Task(object):

    def __init__(self, storage):
        self.storage = storage


    def on_get(self, req, res):    
        tasks = self.storage.get_tasks()

        if tasks == None or len(tasks) == 0:
            res.status = falcon.HTTP_200
            res.body = json.dumps({"test":"Not Found"})
        else:
            res.status = falcon.HTTP_200
            res.body = json.dumps(tasks)


    def on_post(self, req, res):
        try:
            raw_json = req.stream.read().decode('utf-8')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

        try:
            param = json.loads(raw_json, encoding='utf-8')

            res.status = falcon.HTTP_201
            res.body = json.dumps(param)
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Invalid JSON',ex.message)


class TaskDetail(object):

    def __init__(self, storage):
        self.storage = storage


    def on_get(self, req, res, task_id):
        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'task': 'todo-task',
            'task_id': task_id
        })
    
    def on_put(self, req, res, task_id):
        res.status = falcon.HTTP_202
        res.body = json.dumps({
            'task': 'todo-task-put',
            'task_id': task_id
        })