# python3

import heapq

class Worker:
    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time

class JobQueue:
    def __init__(self,n_workers,jobs):
        self.n_workers = []
        for i in range(n_workers):
            heapq.heappush(self.n_workers, Worker(i))
        self.jobs = jobs
        self.id_starttime = []
    
    def printThreadIdAndStarttime(self):
        for i, j in self.id_starttime:
            print(i, j)

    def assign_jobs(self):
        for job in self.jobs:
            freeThread = heapq.heappop(self.n_workers)
            self.id_starttime.append((freeThread.thread_id,freeThread.release_time))
            freeThread.release_time += job
            heapq.heappush(self.n_workers, freeThread)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    jobq = JobQueue(n_workers, jobs)
    jobq.assign_jobs()
    jobq.printThreadIdAndStarttime()


if __name__ == "__main__":
    main()
