#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Duy Tran
# -------------------------------

"""
To test the program:
    % python TestPFD.py >& TestPFD.py.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py >& TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import pfd_solve, pfd_addEmpties, pfd_eval, pfd_print

# -----------
# TestCollatz
# -----------
class TestPFD (unittest.TestCase) :
	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
		w = StringIO.StringIO()
		pfd_solve(r, w)
		self.assert_(w.getvalue() == "1 5 3 2 4 \n\n")

	def test_solve_2 (self) :
		r = StringIO.StringIO("10 0")
		w = StringIO.StringIO()
		pfd_solve(r, w)
		self.assert_(w.getvalue() == "1 2 3 4 5 6 7 8 9 10 \n\n")

	def test_solve_3 (self) :
		r = StringIO.StringIO("3 2\n1 2 2 3\n2 1 3")
		w = StringIO.StringIO()
		pfd_solve(r, w)
		self.assert_(w.getvalue() == "3 2 1 \n\n")

	def test_solve_4 (self) :
		r = StringIO.StringIO("10 6\n8 5 10 1 7 3 2\n2 1 10\n9 2 7 8\n6 4 1 8 5 3\n4 7 7 2 1 5 3 9 6\n1 1 3")
		w = StringIO.StringIO()
		pfd_solve(r, w)
		self.assert_(w.getvalue() == "3 1 5 7 10 2 8 6 9 4 \n\n")

	# ----------
	# addEmpties
	# ----------

	def test_addEmpties_1 (self) :
		index = -1
		avail = []
		numDep = [0, 0, 0, 0, 0]
		count = pfd_addEmpties(index, avail, numDep)
		self.assert_(index == -1)
		self.assert_(str(avail) == "[1, 2, 3, 4]")
		self.assert_(str(numDep) == "[0, -1, -1, -1, -1]")
		self.assert_(count == 4)

	def test_addEmpties_2 (self) :
		index = 4
		avail = []
		numDep = [0, 2, 2, 1, 0]
		count = pfd_addEmpties(index, avail, numDep)
		self.assert_(index == 4)
		self.assert_(str(avail) == "[4]")
		self.assert_(str(numDep) == "[0, 2, 2, 1, -1]")
		self.assert_(count == 1)

	def test_addEmpties_3 (self) :
		index = 1
		avail = []
		numDep = [0, 0]
		count = pfd_addEmpties(index, avail, numDep)
		self.assert_(index == 1)
		self.assert_(str(avail) == "[1]")
		self.assert_(str(numDep) == "[0, -1]")
		self.assert_(count == 1)

	def test_addEmpties_4 (self) :
		index = -1
		avail = []
		numDep = [0, 0, 5, 0, 0, 2, 0, 2, 0]
		count = pfd_addEmpties(index, avail, numDep)
		self.assert_(index == -1)
		self.assert_(str(avail) == "[1, 3, 4, 6, 8]")
		self.assert_(str(numDep) == "[0, -1, 5, -1, -1, 2, -1, 2, -1]")
		self.assert_(count == 5)

	# ----
	# eval
	# ----

	def test_eval_1 (self) :
		nodes = {1: [3, 5], 2: [], 3: [2, 4], 4: [], 5: [3, 2]}
		numDep = [0, 0, 2, 2, 1, 1]
		answer = [0, 0, 0, 0, 0]
		n = 5
		pfd_eval(nodes, numDep, answer, n)
		self.assert_(n == 5)
		self.assert_(str(nodes) == "{1: [3, 5], 2: [], 3: [2, 4], 4: [], 5: [3, 2]}")
		self.assert_(str(numDep) == "[0, -1, -1, -1, -1, -1]")
		self.assert_(str(answer) == "[1, 5, 3, 2, 4]")
		
	def test_eval_2 (self) :
		nodes = {1: [8, 6, 4], 2: [8, 4], 3: [8, 6, 4, 1], 4: [], 5: [6, 4], 6: [4], 7: [8, 9, 4], 8: [9, 6], 9: [4], 10: [8, 2]}
		numDep = [0, 1, 1, 0, 7, 0, 4, 0, 5, 2, 0]
		answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		n = 10
		pfd_eval(nodes, numDep, answer, n)
		self.assert_(n == 10)
		self.assert_(str(nodes) == "{1: [8, 6, 4], 2: [8, 4], 3: [8, 6, 4, 1], 4: [], 5: [6, 4], 6: [4], 7: [8, 9, 4], 8: [9, 6], 9: [4], 10: [8, 2]}")
		self.assert_(str(numDep) == "[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]")
		self.assert_(str(answer) == "[3, 1, 5, 7, 10, 2, 8, 6, 9, 4]")

	def test_eval_3 (self) :
		nodes = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
		numDep = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		n = 10
		pfd_eval(nodes, numDep, answer, n)
		self.assert_(n == 10)
		self.assert_(str(nodes) == "{1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}")
		self.assert_(str(numDep) == "[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]")
		self.assert_(str(answer) == "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")

	def test_eval_4 (self) :
		nodes = {1: [], 2: [5], 3: [], 4: [5, 1, 2], 5: [1], 6: [1], 7: [], 8: [5, 1], 9: [5, 1, 2], 10: [5], 11: [1], 12: [1], 13: [1], 14: [1], 15: [], 16: [1], 17: [5], 18: [1]}
		numDep = [0, 11, 2, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		n = 18
		pfd_eval(nodes, numDep, answer, n)
		self.assert_(n == 18)
		self.assert_(str(nodes) == "{1: [], 2: [5], 3: [], 4: [5, 1, 2], 5: [1], 6: [1], 7: [], 8: [5, 1], 9: [5, 1, 2], 10: [5], 11: [1], 12: [1], 13: [1], 14: [1], 15: [], 16: [1], 17: [5], 18: [1]}")
		self.assert_(str(numDep) == "[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]")
		self.assert_(str(answer) == "[3, 4, 6, 7, 8, 9, 2, 10, 11, 12, 13, 14, 15, 16, 17, 5, 18, 1]")

    # -----
    # print
    # -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		answer = [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 5, 21, 22, 23, 24, 25, 26, 4]
		pfd_print(w, answer)
		self.assert_(w.getvalue() == "1 2 3 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 5 21 22 23 24 25 26 4 \n\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		answer = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 1, 25, 26, 27, 10, 17, 28]
		pfd_print(w, answer)
		self.assert_(w.getvalue() == "2 3 4 5 6 7 8 9 11 12 13 14 15 16 18 19 20 21 22 23 24 1 25 26 27 10 17 28 \n\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		answer = [1]
		pfd_print(w, answer)
		self.assert_(w.getvalue() == "1 \n\n")

	def test_print_4 (self) :
		w = StringIO.StringIO()
		answer = [3, 1, 5, 7, 10, 2, 8, 6, 9, 4]
		pfd_print(w, answer)
		self.assert_(w.getvalue() == "3 1 5 7 10 2 8 6 9 4 \n\n")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
