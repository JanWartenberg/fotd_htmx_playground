from random import random
import time
from threading import Thread


class Downloader:
    preparation_status = "Waiting"
    preparation_progress = 0
    thread = None

    def status(self):
        return Downloader.preparation_status

    def progress(self):
        return Downloader.preparation_progress

    def run(self):
        if Downloader.preparation_status == "Waiting":
            Downloader.preparation_status = "Running"
            Downloader.preparation_progress = 0
            Downloader.thread = Thread(target=self.run_impl)
            Downloader.thread.start()

    def reset(self):
        Downloader.preparation_status = "Waiting"

    @staticmethod
    def run_impl():
        for i in range(10):
            time.sleep(1 * random())
            if Downloader.preparation_status != "Running":
                return
            Downloader.preparation_progress = (i + 1) / 10
            print("Here... " + str(Downloader.preparation_progress))
        time.sleep(0.5)
        if Downloader.preparation_status != "Running":
            return
        Downloader.preparation_status = "Complete"

    @classmethod
    def get(cls):
        return Downloader()

    def download_file(self):
        return r"static\example_fact.json"
