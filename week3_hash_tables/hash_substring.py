# python3
import random

class HashStringSearch:
    _prime = 1000000007
    _multiplier = random.randint(1, _prime)

    def __init__(self,text,pattern):
        self.text = text
        self.pattern = pattern
        self.tlength = len(self.text)
        self.plength = len(self.pattern)
        self.bound = self.tlength - self.plength + 1

    def _hash_func(self, s):
        h = 0
        for c in reversed(s):
            h = (h * self._multiplier + ord(c)) % self._prime
        return h 
    
    def _precompute_hashes(self):
        H = [0] * self.bound
        H[self.bound-1] = self._hash_func(self.text[-self.plength:])
        y = 1
        for _ in range(1, self.plength+1):
            y = (y * self._multiplier) % self._prime
        for i in range(self.bound-2,-1,-1):
            prehash = self._multiplier * H[i + 1] + ord(text[i]) - y * ord(self.text[i + self.plength])
            while prehash < 0:
                prehash += self._prime
            H[i] = prehash % self._prime
        return H

    def get_occurrences(self):
        res = []
        phash = self._hash_func(self.pattern)
        H = self._precompute_hashes()
        print(H)

        for i in range(self.bound):
            if phash == H[i] and text[i:i+len(pattern)] == pattern:
                res.append(i)
        return res

if __name__ == '__main__':
    pattern, text = input().rstrip(), input().rstrip()
    hss = HashStringSearch(text, pattern)
    res = hss.get_occurrences()
    print(" ".join(map(str, res)))