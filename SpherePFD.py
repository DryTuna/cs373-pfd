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


def pfd_solve (r, w) :
	"""
	reads lines of ints into their appropriate arrays
	r is a reader
	nodes is a list containing lists of edges according to the number of nodes
	avail is a list of nodes that contain no edges 
	return true if that succeeds, false otherwise
	"""
	s = r.readline()
	while (s != ""):
		l = s.split()
		n = int(l[0])
		c = int(l[1])
	
		nodes = {}
		for x in range(1, n+1) :
			nodes[int(x)] = []

		numDep = [0]*(n+1)
		answer = [0]*n

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

		pfd_eval(w, nodes, numDep, answer, n)

		s = r.readline()
		if (s == "\n") :
			s = r.readline()

		pfd_print(w, answer)


def pfd_addEmpties (index, avail, numDep) :
	"""
	Adds nodes with no edges to the list of available nodes
	avail is a list of nodes that contain no edges
	numDep is the list containing the number of dependencies (edges) leading to each node
	"""
	count = 0
	if (index == -1) :
		for x in range (1, len(numDep)):
			if numDep[x] == 0:
				numDep[x] = -1
				heappush(avail, x)
				count += 1
	else :
		numDep[index] = -1
		heappush(avail, index)
		count += 1
	return count

					
def pfd_eval(w, nodes, numDep, answer, n) :
	avail = []
	totalCount = n
	answerIndex = 0;

	while totalCount > 0 :
		totalCount -= pfd_addEmpties(-1, avail, numDep)
		while len(avail) > 0 :
			answer[answerIndex] = heappop(avail)
			for y in nodes[answer[answerIndex]]:
				numDep[y] -= 1
				if (numDep[y] == 0) :
					totalCount -= pfd_addEmpties(y, avail, numDep)
			answerIndex += 1


def pfd_print(w, answer) :
	"""
	prints order of tasks
	w is a writer
	answer is the array that holds the answer	
	"""	
	for x in range(0, len(answer)) :
		w.write(str(answer[x]) + " ")
	w.write("\n\n")
			
pfd_solve(sys.stdin, sys.stdout)
