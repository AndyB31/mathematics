#!/usr/bin/python

from math import *
import sys

def f(x, n):
	k = 0
	c = 1
	while k < n:
		c *= sin(x)
		k += 1
	return (c)
