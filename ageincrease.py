'''
Function to increase age

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def increaseAge(currentdate, age, birthdate):
    currentday = str(currentdate)
    birthday = str(birthdate)
    currentday = currentday[5:10]
    birthday = birthday[5:10]
    if currentday == birthday:
        age += 1
    return age