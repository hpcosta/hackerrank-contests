#!/usr/bin/env python
# -- coding: UTF-8 --

# https://www.hackerrank.com/contests/w28/challenges/boat-trip

import sys

n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
tour_groups = n
boat_capacity = c
n_boats = m

n_passengers = map(int,raw_input().strip().split(' '))
n_passengers.sort()
flag = True
if (len(n_passengers)) > tour_groups:
	flag = False
else:
	for i in n_passengers:
		if i > (boat_capacity*n_boats):
			flag = False

if flag:
	print('Yes')
else:
	print('No')