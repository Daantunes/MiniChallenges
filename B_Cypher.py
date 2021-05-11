#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: B_Cyther.py
# Created Date: Tuesday April 27th 2021
# Author: Debora Antunes & Daniel Martins
# -----
# Last Modified: Tuesday, May 4th 2021
# -----
'''

import sys

def format_message(input_string):
    """
    Formats the input.
    
    Args:
        input_string (string) : The text to be processed.
    
    Return:
        (list, list) : Lists with the keyword and the message, respectivly.
    """
    strings = input_string.upper().split('\n')
    message = list(filter(str.isalpha, "".join(strings[1:])))
    return strings[0], message

def cols(input_string):
    """
    Create a dictionary to cypher and prepare the output.
    
    Args:
        input_string (string) : The text to be processed.
    """
    key, message = format_message(input_string)
    k = len(key)
    m = len(message)
    chunks = [message[i:i+k] for i in range(0, m, k)]

    key_letters = dict(map(lambda x: (x, []), key))
    for word in chunks:
        for l in range(len(word)):
                key_letters[key[l]] += word[l]
    
    final_message = ''.join(list(map(lambda l: ''.join(key_letters[l]), sorted(key_letters))))
    final_message = [final_message[i:i+5] for i in range(0, m, 5)]
    final_sentences = "\n".join([" ".join(final_message[i:i+8]) for i in range(0, len(final_message), 8)])
    print(final_sentences)

cols(sys.stdin.read())