class Worker:

    def work(self):
        print("I'm working!!")


class SuperWorker(Worker):

    def work(self):
        print("I work very hard!!!")


class BadWorker(Worker):
    def work(self):
        print("I forgot to work!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
bad_worker = BadWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
    manager.set_worker(bad_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
