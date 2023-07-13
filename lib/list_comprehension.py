#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [n for n in num_list if n % 2 == 0]
    return evens_list

def make_exclamation(sentence_list):
    exclamation_list = []
    for sentence in sentence_list:
        exclamation_list.append(sentence + '!')
    return exclamation_list