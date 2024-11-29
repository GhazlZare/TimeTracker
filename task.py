import uuid
from datetime import datetime

class Task:
    def __init__(self, name, description, project_association):
        self.name = name
        self._task_id = str(uuid.uuid4())
        self.description = description
        self.status = False
        self.start_t = datetime.now()
        self.end_t = None
        self.duration = None
        self.prj_association = project_association

    @property
    def task_id(self):
        return self._task_id
    
    def mark_done(self):
        self.end_t = datetime.now()
        self.status = True

    def task_duration(self):
        if self.start_t and self.end_t:
            self._duration = (self.end_t - self.start_t).total_seconds() / 3600
        return self.duration
    
    def __str__(self):
        status = "Done" if self.status else "Not Done"
        return (f"Task ID: {self.task_id}, Name: {self.name}, Status: {status}, "
                f"Start: {self.start_t}, End: {self.end_t}")