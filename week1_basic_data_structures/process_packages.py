# python3

from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        # write your code here
        while self.finish_time and self.finish_time[0] <= request.arrival_time:
            self.finish_time.popleft()
        if len(self.finish_time) == self.size:
            return Response(True,-1)
        if self.finish_time:
            self.finish_time.append(self.finish_time[-1]+request.process_time)
            return Response(False,self.finish_time[-2])
        else:
            self.finish_time.append(request.arrival_time+request.process_time)
            return Response(False,request.arrival_time)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    main()
