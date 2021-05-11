#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: C_BinaryTree.py
# Created Date: Tuesday April 27th 2021
# Author: Debora Antunes & Daniel Martins
# -----
# Last Modified: Tuesday, May 4th 2021
# -----
'''

import sys
sys.setrecursionlimit(100001)

def post_order(L, out_ordered):
    """
    Cretes the list of post-order transversal.
    
    Args:
        L (list) : List of numbers with the preorder transversal.
        out_ordered (list) : List of numbers with the post-order transversal.
        
    Return:
        (list) : List of numbers with the post-order transversal.
        
    """
    root = L[0]
    left = 1 if L[1] <= L[0] else None
    right = find_right_pivot(L, root)
    
    if left is not None:
        if sorted_desc(L[1:right]):
            out_ordered += L[1:right][::-1]
            left = None
        else:
            out_ordered = post_order(L[1:right], out_ordered)
            left = None
            
    if right is not None:
        if sorted_asc(L[right:]):
            out_ordered += L[right:][::-1]
            right = None
        else:
            out_ordered = post_order(L[right:], out_ordered)
            right = None
            
    if left is None and right is None: 
        out_ordered += [root]
        return out_ordered

def find_right_pivot(sub, root):
    """
    Finds the index of the first greater number after the root.
    
    Args:
        sub (list) : Sub-list with numbers associated with a specific root.
        root (int) : The value of the root.
        
    Return:
        (int) : Index of the first number greater than the root. 
    """
    for i in range(1, len(sub)):
        if sub[i] > root:
            return i
    return None

def sorted_desc(sub):
    """
    Tests if the numbers are sorted in ascending order.
    
    Args:
        sub (list) : Sub-list with numbers associated with a specific root.
    
    Return:
        (boolean): True if the section is sorted in ascending order.
    
    """
    for i in range(len(sub)-1):
        if sub[i] < sub[i+1]:
            return False
    return True

def sorted_asc(sub):
    """
    Tests if the numbers are sorted in descending order.
    
    Args:
        sub (list) : Sub-list with numbers associated with a specific root.
    
    Return:
        (boolean): True if the section is sorted in descending order.
    
    """
    for i in range(len(sub)-1):
        if sub[i] >= sub[i+1]:
            return False
    return True

def run(inp):
    """
    Runs the algorithm staring with receiving the input, sendig the list to post_order and printing the final list.
    
    Args:
        inp (string) : Sequence of number separated with a space, ordered in preorder.
    """
    all_L = [int(x) for x in inp.strip().split(' ')]
    out  = post_order(all_L, [])
    print(" ".join(map(str, out)))


run(sys.stdin.read())