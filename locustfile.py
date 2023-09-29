from locust import HttpUser, task, between

class WeatherAppUser(HttpUser):
    wait_time = between(1, 5)  # Attend entre 1 et 5 secondes entre les tâches

    @task
    def index(self):
        self.client.get("/")
