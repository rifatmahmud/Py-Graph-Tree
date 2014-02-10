#!/usr/bin/env python

import numpy as np
import math
import collections
import sys

def generate_set_of_points(dimensions, number_of_points):
	
	pt_set=[0]

	for j in range(0, number_of_points-1):
		pt_set.append(0)
	
	for i in range(0, number_of_points):
		
		np.random.seed()
		pt=[0]
		
		for j in range(0, dimensions-1):
			pt.append(0)
		
		for j in range(0, dimensions):
			pt[j]=np.random.uniform(-25000, 25000)
		
		pt_set[i]=pt

	kdtree=[None]*number_of_points	
	
	return pt_set


def determine_level(number_of_points):
	s=0
	
	for i in range(0, number_of_points):
		s=s+math.pow(2, i)
		if number_of_points<=s
			s=s-math.pow(2, i)
			break
	
	return s
		

def find_median(pt_set, current_dimension):	
	
	sum=0
	if len(pt_set)==0
		return None
	for pt in pt_set:
		sum=sum+pt[current_dimension-1]
	
	mean=sum/len(pt_set)
	min=sys.maxint
	
	for pt in pt_set:
		
		if min>abs(pt[current_dimension-1]-mean):
			min=abs(pt[current_dimension-1]-mean)
	
	return min
	
def create_subtree(root_pt, pt_set, current_dim):

	for pt in pt_set:
	
		if pt[current_dim]<root_pt[current_dim]:
			left_tree.append(pt)
		else:
			right_tree.appen(pt)
	
	return [left_tree, right_tree]
	


def construct_kdtree(dimensions, pt_set, root_pos, current_dimension, current_level, current_pos, num_of_level, kdtree):
	
	if root_pos==0:
		num_of_level=determine_level(len(pt_set))
		size=math.pow(2, num_of_level)-1
		kdtree=[None]*size
		
	if current_dimension==dimensions+1
		current_dimension=1
	
	if num_of_level<current_level
		return
	for i in range(0, math.pow(2, current_level))
		

	median=find_median(pt_set, current_dimension)
	kdtree[root_pos]=median
	if current_level==number_of_level
		return
	[pt_set_left, pt_set_right]=create_subtree(median, pt_set, current_dimension)
	construct_kdtree(dimensions, pt_set_left, 2*root_pos+1, current_dimension+1, current_level+1, num_of_level, kdtree)
	construct_kdtree(dimensions, pt_set_right, 2*root_pos+2, current_dimension+1, current_level+1, num_of_level, kdtree)
	
	
		
		
		if
	else:
		if(pt
	if current_level<num_of_level:
		[pt_set_left, pt_set_right]=create_subtree(median, pt_set, current_dimension)
		median=find_median(pt_set, current_dimension)
		kdtree[root_pos]=
		
	if current_level<num_of_level:
		
		
	