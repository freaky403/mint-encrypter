import queue
import threading


class Worker(threading.Thread):
    def __init__(self, q):
        self.q = q
        super().__init__()

    def run(self):
        while True:
            try:
                f = self.q.get(timeout=3)
            except queue.Empty:
                return

            f()
            self.q.task_done()
