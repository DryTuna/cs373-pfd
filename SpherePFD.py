#!/usr/bin/env python

"""
To run the program
% python RunPFD.py < RunPFD.in > RunPFD.out

To document the program
% pydoc -w PFD
"""

# -------
# imports
# -------

import sys

from heapq import heappush, heappop


def pfd_start (r, w) :
	"""
	Read, eval, print
	r is a reader
	w is a writer
	"""
	totalCount = [0]
	edges = []
	avail = []
	nodes = []
	pfd_read(r, w, nodes, totalCount, avail)
	

def pfd_read (r, w, nodes, totalCount, avail) :
	"""
	reads lines of ints into their appropriate arrays
	r is a reader
	nodes is a list containing lists of edges according to the number of nodes
	avail is a list of nodes that contain no edges 
	return true if that succeeds, false otherwise
	"""

	s = r.readline()
	if s == "" :
		return False
	l = s.split()
	n = int(l[0])
	c = int(l[1])
	
	nodes = {}
	for x in range(1, n+1) :
		nodes[int(x)] = []

	numDep = [0]*(n+1)
	answer = [0]*n
	totalCount[0] = n
	
	while c > 0 :
		s = r.readline()
		l = s.split()
		vert = int(l[0])
		x = int(l[1])
		numDep[vert] = x
		temp = [0]
		for y in range (2, len(l)):
			nodes[int(l[y])].append(vert)
		
		c -= 1
	

	pfd_eval(w, nodes, numDep, avail, answer, totalCount)
	return True


def pfd_addEmpties (avail, numDep, nodes) :
	"""
	Adds nodes with no edges to the list of available nodes
	avail is a list of nodes that contain no edges
	numDep is the list containing the number of dependencies (edges) leading to each node
	"""
	for x in range (1, len(numDep)):
		if numDep[x] == 0:
			numDep[x] = -1
			heappush(avail, x)

					
def pfd_eval(w, nodes, numDep, avail, answer, totalCount) :
	
	answerIndex = 0;
	pfd_addEmpties(avail, numDep, nodes)
	while totalCount[0] > 0 :
		while len(avail) > 0 :
			answer[answerIndex] = heappop(avail)
			for y in nodes[answer[answerIndex]]:
				numDep[y] -= 1
			answerIndex += 1
			totalCount[0] -= 1
		pfd_addEmpties(avail, numDep, nodes)

	pfd_print(w, answer)

def pfd_print(w, answer) :
	"""
	prints order of tasks
	w is a writer
	answer is the array that holds the answer	
	"""	

	for x in range(0, len(answer)) :
		w.write(str(answer[x]) + " ")
			
			
pfd_start(sys.stdin, sys.stdout)