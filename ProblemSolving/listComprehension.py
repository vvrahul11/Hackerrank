#!/bin/python3

# list comprehension

# square numbers in a list
square = [i **2 for i in range(10)]

# square numbers in a list if divisible by 3
square = [i **2 for i in range(30) if i % 3 == 0]

#Change value to key and vice versa
capitals = {'United States': 'Washington, DC','France': 'Paris','Italy': 'Rome'}
capitals_bycapital = {capitals[key]: key for key in capitals}
