#!/usr/bin/python

from math import *
import sys

def f(x, n):
	if x == 0:
		return (1)
	k = 0
	c = float(1)
	while k < n + 1:
		c *= (sin(x / (2 * k + 1))) / (x / (2 * k + 1))
		k += 1
	return (c)
