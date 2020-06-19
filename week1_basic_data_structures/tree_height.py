# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.height = [0] * self.n

    def compute_height(self):
        maxHeight = -1
        for node in range(self.n):
            maxHeight = max(maxHeight,self.get_node_height(node))
        return maxHeight
        

    def get_node_height(self,node):
        if self.parent[node] == -1:
            return 1
        if self.height[node]:
            return self.height[node]
        else:
            self.height[node] = self.get_node_height(self.parent[node]) + 1
            return self.height[node]


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()