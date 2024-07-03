import json
# import threading
import os
from subprocess import Popen
import time


class ServiceHandler():
    def __init__(self, path: str = None) -> None:
        if path:
            self.load_services(path)
        else:
            self.load_services()
        self.process_list = []

    def load_services(self, path="services.json"):
        _services = json.loads(open(path).read())
        self.services = []

        for name in _services:
            service = _services.get(name)
            service["status"] = "stopped"
            service["id"] = name
            self.services.append(service)

    def start_service(self, id) -> bool:
        service = self.get_service(id)
        if service:
            service["status"] = "running"
            print(service["start_command"])
            process = Popen(service["start_command"])
            self.process_list.append(
                {"id": id, "process": process})
            return True
        return False

    def stop_service(self, id) -> bool:
        service = self.get_service(id)
        if service:
            service["status"] = "stopped"
            process = self.get_process(id)
            print(process)
            if process:
                process.kill()
                self.remove_process(id)
                print(self.process_list)
            if service.get("stop_command"):
                os.system(" ".join(service.get("stop_command")))
            return True
        return False

    def get_process(self, id):
        for process in self.process_list:
            if process["id"] == id:
                return process["process"]
        return None

    def get_service(self, id):
        for service in self.services:
            if service["id"] == id:
                return service
        return None

    def remove_process(self, id):
        for i, process in enumerate(self.process_list):
            if process["id"] == id:
                self.process_list.pop(i)
                return True
        return False

# class ServiceThread(threading.Thread):
#     def __init__(self, service: dict) -> None:
#         threading.Thread.__init__(self)
#         self.service = service

#     def run(self):
#         for command in self.service.start_command:
#             os.system(command)

#     def kill(self):
#         self.service["status"] = "stopped"
#         raise Exception("Killed Service Thread: " +
#                         str(self.service.get("name")))

#     def get_id(self):
#         return self.service.get("id")


SERVICE_HANDLER = ServiceHandler()
