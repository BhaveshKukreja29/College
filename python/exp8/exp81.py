"""
Python program to demonstrate use of regular expression 

● Create string with name of cities in india separated by spaces. 

● Find all cities ending with “ai”

● Find all cities starting with “Mu” or “Ma”
"""

import re

cities = input("Enter cities seperated by spaces: ").split()

aic = []
muma = []

for city in cities:
    if re.search(".+ai$", city):
        aic.append(city)
    if re.search("^mu.+", city) or re.search("^ma.+", city):
        muma.append(city)

print(aic)
print(muma)
