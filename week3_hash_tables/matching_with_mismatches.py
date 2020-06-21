# python3

import sys
import random

class Solver:
	_m1 = pow(10,9) + 7
	# _m2 = pow(10,9) + 9
	_multiplier = random.randint(1,_m1)

	def __init__(self, k, t, p):
		self.t = "#" + t
		self.p = "#" + p
		self.k = int(k)
		self.tH1 = self._precompute_hashes(self.t)
		self.pH1 = self._precompute_hashes(self.p)
		
		# self.tH1 ,self.tH2 = self._precompute_hashes(self.t)
		# self.pH1, self.pH2 = self._precompute_hashes(self.p)

	def _precompute_hashes(self,s):
		n = len(s)
		H1 = [0]
		# H2 = [0]

		for i in range(1,n):
			H1.append((H1[i-1] * self._multiplier + ord(s[i])) % self._m1)
			# H2.append((H1[i-1] * self._multiplier + ord(s[i])) % self._m2)
		return H1#,H2

	def _hash_partial_m1(self,H,a,l):
		return  (H[a+l-1] - (H[a-1]*pow(self._multiplier,l,self._m1))) % self._m1
	
	# def _hash_partial_m2(self,H,a,l):
	# 	return  (H[a+l-1] - (H[a-1]*pow(self._multiplier,l,self._m2))) % self._m2


	def binary_search(self,start,end,shift):
		if start == end:
			if self.t[start] == self.p[start-shift]:
				return 0
			else:
				return 1
		
		mid = start + (end-start)//2
		th1l = self._hash_partial_m1(self.tH1,start,mid-start+1)
		# th2l = self._hash_partial_m2(self.tH2,start,mid-start+1)
		ph1l = self._hash_partial_m1(self.pH1,start-shift,mid-start+1)
		# ph2l = self._hash_partial_m2(self.pH2,start-shift,mid-start+1)
		th1r = self._hash_partial_m1(self.tH1,mid+1,end-mid)
		# th2r = self._hash_partial_m2(self.tH2,mid+1,end-mid)
		ph1r = self._hash_partial_m1(self.pH1,mid+1-shift,end-mid)
		# ph2r = self._hash_partial_m2(self.pH2,mid+1-shift,end-mid)

		if th1l == ph1l: # and th2l == ph2l:
			l = 0
		else:
			l = self.binary_search(start,mid,shift)

		if th1r == ph1r: # and th2r == ph2r:
			r = 0
		else:
			r = self.binary_search(mid+1,end,shift)

		if l == -1 or r == -1: return -1
		if l + r > self.k: 
			return -1
		else:
			return l + r

	def solve(self):
		res = []
		for i in range(1,len(self.t)-len(self.p)+2):
			if self.binary_search(i,i+len(self.p)-2,i-1) != -1:
				res.append(i-1)
		return res
	


for line in sys.stdin.readlines():
	k, t, p = line.split()
	solver = Solver(k,t,p)
	res = solver.solve()
	print(len(res), *res)
