from locust import HttpUser, task, between
from time import sleep


class HelloWorldUser(HttpUser):

    # wait time between 1 and 5 seconds after each task
    wait_time = between(1, 5)

    # task with higher weight are performed more frequently
    # this task will be performed 3 times more than the others
    # this task will visit the /hello and /locust paths
    @task(3)
    def hello_locust(self):
        self.client.get("/hello")
        self.client.get("/locust")

    # task with lower weight are performed less frequently
    # this task will list through 10 "items" with item_id from 0 to 9
    @task
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            sleep(1)
