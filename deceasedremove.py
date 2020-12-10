'''
Function to delete deceased citizen from the list

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def deleteDeceased(objs, citizen):
    if citizen.alive == 0:
        objs.remove(citizen)
    return objs

    