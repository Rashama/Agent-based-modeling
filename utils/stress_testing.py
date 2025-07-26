from locust import HttpUser, task, between

class StreamlitUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_main_page(self):
        self.client.get("/")  # Adjust the path if needed
