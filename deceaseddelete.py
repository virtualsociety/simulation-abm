'''
Function to delete deceased

By Dr. Raymond Hoogendoorn
Copyrigh t2020
'''

def deleteDeceased(citizen, objs):
    if citizen.alive == 0:
        objs.remove(citizen)
    return objs