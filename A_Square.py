#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: A_Square.py
# Created Date: Tuesday April 27th 2021
# Author: Debora Antunes & Daniel Martins
# -----
# Last Modified: Tuesday, May 4th 2021
# -----
'''

import sys

def find_square(text):
    """
    Reads the sequence of numbers to create a matrix and find the biggest square.
    
    Args:
        text (string): Matrix of zeros and ones.
    """
    M = text.strip().split('\n')
    S = [[int(M[j][i]) for i in range(len(M[0]))] for j in range(len(M))]

    for i in range(1, len(S)):
        for j in range(1, len(S[0])):
            if S[i][j] == 1:
                S[i][j] += min(S[i][j-1], S[i-1][j], S[i-1][j-1])

    print(max([max(s) for s in S]))
    
        
inp = sys.stdin.read()
find_square(inp)