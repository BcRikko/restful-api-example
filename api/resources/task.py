import os
import json
import falcon
import datetime

class Task(object):

    def __init__(self, storage):
        self.storage = storage


    def on_get(self, req, res):    
        tasks = self.storage.get_tasks()

        if tasks == None or len(tasks) == 0:
            res.status = falcon.HTTP_200
            res.body = "no data"

        else:
            tasks_dict = []
            for task in tasks:
                task_dict = {
                    "id": task.id,
                    "name": task.name,
                    "remark": task.remark,
                    "deadline": task.deadline.isoformat(),
                    "done": task.done
                }
                tasks_dict.append(task_dict)

            res.status = falcon.HTTP_200
            res.body = json.dumps(tasks_dict)


    def on_post(self, req, res):
        try:
            raw_json = req.stream.read().decode("utf-8")
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_409, "Error", ex)
        
        try:
            param = json.loads(raw_json, encoding="utf-8")
            new_id = self.storage.create_task(param)

            if new_id:
                param["id"] = new_id
                res.status = falcon.HTTP_201
                res.body = json.dumps(param)
            else:
                res.status = falcon.HTTP_409

        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,"Invalid JSON",ex)


class TaskDetail(object):

    def __init__(self, storage):
        self.storage = storage


    def on_get(self, req, res, task_id):
        task = self.storage.get_task(task_id)

        if task:
            task_dict = {
                "id": task.id,
                "name": task.name,
                "remark": task.remark,
                "deadline": task.deadline.isoformat(),
                "done": task.done
            }
            res.status = falcon.HTTP_200
            res.body = json.dumps(task_dict)

        else:
            res.status = falcon.HTTP_404
            res.body = "no data"
    
    
    def on_put(self, req, res, task_id):
        try:
            raw_json = req.stream.read().decode("utf-8")
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_409, "Error", ex)

        try:
            param = json.loads(raw_json, encoding="utff-8")
            success = self.storage.update_task(task_id, param)

            if success:
                res.status = falcon.HTTP_202
                res.body = json.dumps(param)
            else:
                res.status = falcon.HTTP_409
        
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,"Invalid JSON",ex)
    

    def on_delete(self, req,  res, task_id):
        success = self.storage.delete_task(task_id)

        if success:
            res.status = falcon.HTTP_202
        else:
            res.status = falcon.HTTP_409