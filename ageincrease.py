'''
Function to increase age

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def increaseAge(currentdate, age, birthdate, citizen):
    currentday = str(currentdate)
    birthday = str(birthdate)
    currentday = currentday[5:10]
    birthday = birthday[5:10]
    if currentday == birthday and citizen.alive == 1:
        age += 1
    return age