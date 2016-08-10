import falcon

import storage
from resources.task import Task, TaskDetail

api = falcon.API()
api.add_route('/task', Task(storage))
api.add_route('/task/{task_id}', TaskDetail(storage))
