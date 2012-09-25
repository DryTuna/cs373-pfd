#!/usr/bin/env python

"""
To run the program
% python RunPFD.py < RunPFD.in > RunPFD.out
% chmod ugo+x RunPFD.py
% RunPFD.py < RunPFD.in > RunPFD.out

To document the program
% pydoc -w PFD
"""

# -------
# imports
# -------

import sys
import random

def printing(w) :
	"""
	prints order of tasks
	w is a writer
	answer is the array that holds the answer	
	"""	
	for abc in range (1, 50) :
		size = random.randint(1,100)
		curr_list = []
		for x in range (1, size+1) :
			curr_list.append(int(x))
		for x in range (1, size) :
			a = random.randint(0, size-1)
			b = random.randint(0, size-1)
			temp = curr_list[a]
			curr_list[a] = curr_list[b]
			curr_list[b] = temp
		c = random.randint(0, size-1)
		w.write(str(size)+" "+str(c)+"\n")
		temp_list = curr_list[:]
		for x in range (0, c):
			index = random.randint(2,size-1)
			while temp_list[index] < 0 :
				index = random.randint(2, size-1)
			temp_list[index] = -1
			dep = random.randint(1, index)		
			s = str(curr_list[index])+" "+str(dep)
			temp_list2 = curr_list[:]
			temp_list2[index] = -1
			for y in range (0, dep) :
				a = random.randint(0, index-1)
				while temp_list2[a] < 0 :
					a = random.randint(0, index-1)
				temp_list2[a] = -1
				s += " "+str(curr_list[a])
			w.write(s+"\n")
		w.write("\n")
"""
	result = "\n"
	for x in range (0, size) :
		result += str(curr_list[int(x)]) + " "
	print result
"""
	
# ----
# main
# ----
printing(sys.stdout)
