# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "add":
            hashValue = self._hash_func(query.s)
            if query.s not in self.buckets[hashValue]:
                self.buckets[hashValue].append(query.s)
        elif query.type == "del":
            hashValue = self._hash_func(query.s)
            bucket = self.buckets[hashValue]
            for i in range(len(bucket)):
                if bucket[i] == query.s:
                    bucket.pop(i)
                    break
        elif query.type == "find":
            hashValue = self._hash_func(query.s)
            if query.s in self.buckets[hashValue]:
                print("yes")
            else:
                print("no")
        elif query.type == "check":
            print(" ".join(reversed(self.buckets[query.ind])))

    def process_queries(self):
        n = int(input())
        for _ in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
