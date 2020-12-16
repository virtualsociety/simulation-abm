'''
Function to create births

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

#Create the class citizen
class Citizen:
    def __init__(self, ID, gender, age, birthdate, lifeexpectancyprobability, maritalstatus, marriageduration,
                 marriageenddate, marriageintention, marriageage, marriagedate, employmentstatus, income, 
                 capital, children, nrchildren, birthage, birthingdate, alive, event):
        self.ID = ID
        self.gender = gender
        self.age = age
        self.birthdate = birthdate
        self.lifeexpectancyprobability = lifeexpectancyprobability
        self.maritalstatus = maritalstatus
        self.marriageduration = marriageduration
        self.marriageenddate = marriageenddate
        self.marriageintention = marriageintention
        self.marriageage = marriageage
        self.marriagedate = marriagedate
        self.employmentstatus = employmentstatus
        self.income = income
        self.capital = capital
        self.children = children
        self.nrchildren = nrchildren
        self.birthage = birthage
        self.birthingdate = birthingdate
        self.alive = alive
        self.event = event

def generateBirths(currentdate, birthingdate, citizen, objs, df):
    currentday = str(currentdate)
    birthingday = str(birthingdate)
    currentday = currentday[:10]
    birthingday = birthingday[:10]
    return df, citizen, objs