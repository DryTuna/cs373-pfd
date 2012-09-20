#!/usr/bin/env python

import heapq

def pfd_start (r, w) :
	"""
	Read, eval, print loop
	r is a reader
	w is a writer
	"""
	
	edges = []
	avail = []
	answer = []
	nodes = []
	pfd_read(r, edges, avail, nodes)
	pfd_eval(....)
	pfd_print(w, ....)
	

def pfd_read (r, edges, avail, nodes) :
	"""
	reads lines of ints into their appropriate arrays
	r is a reader
	nodes is a list containing lists of edges according to the number of nodes
	avail is a list of nodes that contain no edges 
	return true if that succeeds, false otherwise
	"""

	s = r.readline()
	if s = "" :
		return False
	l = s.split()
	n = int(l[0])
	c = int(l[1])
	
	nodes = nodes[[0]]*(n+1)
	
	while c > 0 :
		s = r.readline()
		l = s.split()
		vert = int(l[0])
		n = int(l[1])
		for x in range (2, len(l)):
			nodes[vert].append(int(l[x]))
		c -= 1
	
	c = 1
	for x in nodes:
		if len(x) == 1:
			heappush(avail, c)
		c += 1
			
		

