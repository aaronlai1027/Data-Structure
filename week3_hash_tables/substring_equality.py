# python3

import sys
import random


class Solver:
	_m1 = pow(10,9) + 7
	_m2 = pow(10,9) + 9
	_multiplier = random.randint(1,_m2)
	

	def __init__(self, s):
		self.s = "#" + s
		self.h1, self.h2 = self._precompute_hashes()

	def _precompute_hashes(self):
		n = len(self.s)
		H1 = [0]
		H2 = [0]

		for i in range(1,n):
			H1.append((H1[i-1] * self._multiplier + ord(self.s[i])) % self._m1)
			H2.append((H2[i-1] * self._multiplier + ord(self.s[i])) % self._m2)
		return H1, H2

	def ask(self, a, b, l):
		h = [0] * 4
		h[0] = (self.h1[a+l] - (self.h1[a]*pow(self._multiplier,l,self._m1))) % self._m1
		h[1] = (self.h2[a+l] - (self.h2[a]*pow(self._multiplier,l,self._m2))) % self._m2
		h[2] = (self.h1[b+l] - (self.h1[b]*pow(self._multiplier,l,self._m1))) % self._m1
		h[3] = (self.h2[b+l] - (self.h2[b]*pow(self._multiplier,l,self._m2))) % self._m2

		if h[0] == h[2] and h[1] == h[3]:
			return True
		else:
			return False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
