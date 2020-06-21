# python3

import sys
import random

class CommonSubstring:
	_m1 = pow(10,9)+7
	_m2 = pow(10,9)+9
	_multiplier = random.randint(1, _m2)

	def __init__(self,s,t):
		if len(s) > len(t):
			self.s = "#" + t
			self.t = "#" + s
			self.swap = True
		else:
			self.s = "#" + s
			self.t = "#" + t
			self.swap = False

	def solve(self):
		return self.binary_search(self.s,self.t)

	def _hash_func(self, s):
		h1 = 0
		h2 = 0
		for c in reversed(s):
			h1 = (h1 * self._multiplier + ord(c)) % self._m1
			h2 = (h2 * self._multiplier + ord(c)) % self._m2
		return h1, h2 

	def _precompute_hashes(self,s,length):
		bound = len(s) - length + 1
		H1 = [0] * bound
		H2 = [0] * bound

		hashtable1 = {}
		hashtable2 = {}
		
		H1[bound-1], H2[bound-1] = self._hash_func(s[-length:])

		hashtable1[H1[bound-1]], hashtable2[H2[bound-1]] = bound-1,bound-1
		y1 = pow(self._multiplier,length,self._m1)
		y2 = pow(self._multiplier,length,self._m2)

		for i in range(bound-2,0,-1):
			H1[i] = (self._multiplier * H1[i + 1] + ord(s[i]) - y1 * ord(s[i + length])% self._m1) % self._m1
			H2[i] = (self._multiplier * H2[i + 1] + ord(s[i]) - y2 * ord(s[i + length])% self._m2) % self._m2
			hashtable1[H1[i]],hashtable2[H2[i]] = i,i
		return hashtable1,hashtable2

	def has_common(self,s,t,length):
		H1,H2 = self._precompute_hashes(s,length)
		tbound = len(t) - length + 1
		tH1 = [0] * tbound
		tH2 = [0] * tbound
		tH1[tbound-1],tH2[tbound-1] = self._hash_func(t[-length:])
		if tH1[tbound-1] in H1.keys() and tH2[tbound-1] in H2.keys():
			return H1[tH1[tbound-1]], tbound-1, True
		y1 = pow(self._multiplier,length,self._m1)
		y2 = pow(self._multiplier,length,self._m2)
		for i in range(tbound-2 ,0,-1):
			tH1[i] = (self._multiplier * tH1[i + 1] + ord(t[i]) - y1 * ord(t[i + length])) % self._m1
			tH2[i] = (self._multiplier * tH2[i + 1] + ord(t[i]) - y2 * ord(t[i + length])) % self._m2
			if tH1[i] in H1.keys() and tH2[i] in H2.keys():
				return H1[tH1[i]], i, True
		return 1,1,False

	def binary_search(self,s,t):
		l = 1
		r = len(s) - 1
		idx1,idx2,maxLength = 1,1,0
		while l <= r:
			length = l + (r-l)//2
			i1,i2,iscom = self.has_common(s,t,length)
			if iscom:
				l = length + 1
				if length > maxLength:
					idx1 = i1
					idx2 = i2
					maxLength = length
			else:
				r = length - 1
		
		if self.swap:
			return idx2-1, idx1-1, maxLength
		else:
			return idx1-1, idx2-1, maxLength


for line in sys.stdin.readlines():
	s, t = line.split()
	css = CommonSubstring(s, t)
	i,j,l = css.solve()
	print(i,j,l)
