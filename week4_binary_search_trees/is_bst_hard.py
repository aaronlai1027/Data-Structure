#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if not tree: return True
  def helper(root,lowerbound,upperbound):
      if root == -1:
        return True
      if tree[root][0] < lowerbound or tree[root][0] >= upperbound:
        return False
      left = helper(tree[root][1],lowerbound,tree[root][0])
      right = helper(tree[root][2],tree[root][0],upperbound)
      return left and right
  return helper(0,float("-inf"),float("inf"))

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for _ in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
