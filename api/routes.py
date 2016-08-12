import os
import falcon

import storage
from resources.task import Task, TaskDetail

api = falcon.API()
api.add_route("/task", Task(storage))
api.add_route("/task/{task_id}", TaskDetail(storage))


# Windows用
if os.name == "nt" and  __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8080, api)
    httpd.serve_forever()