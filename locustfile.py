from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """on_start is called when the TaskSet is starting"""
        pass

    def on_stop(self):
        """on_stop is called when the TaskSet is stopping"""
        pass

    @task(1)
    def getLatestBlockNumber(self):
        self.client.get(
            "http://localhost:5000/getLatestBlockNumber",
        )

    @task(2)
    def getBlockByNumber(self):
        self.client.post(
            "http://localhost:5000/getBlockByNumber", json={"blockNumber": "0xe156"}
        )

    @task(3)
    def getTransactionByBlockAndIndex(self):
        self.client.post(
            "http://localhost:5000/getTransactionByBlockNumberAndIndex",
            json={"blockNumber": "0xe156", "index": "0x0"},
        )
