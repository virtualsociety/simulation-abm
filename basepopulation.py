'''
Function to create the basepopulation

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import sys

from genderprobability import calculateGenderProbability
from ageprobability import calculateAgeProbability
from lifeexpectancyprobability import calculateLifeExceptancyProbability
from maritalstatusprobability import calculateMaritalStatusProbability
from marriagedurationprobability import calculateMarriageDurationProbability
from marriageageprobability import calculateMarriageAgeProbability
from marriageintentionprobability import calculateMarriageIntentionProbability
from employmentstatusprobability import calculateEmploymentStatusProbability
from incomeprobability import calculateIncomeProbability
from childrenprobability import calculateChildrenProbability
from nrchildrenprobability import calculateNrChildrenProbability
from birthageprobability import calculateBirthAgeProbability
from capitalprobability import calculateCapitalProbability

from gender import generateGender
from age import generateAge
from birthdate import generateBirthdate
from maritalstatus import generateMaritalStatus
from marriageduration import generateMarriageDuration
from marriageenddate import generateMarriageEndDate
from marriageintention import generateMarriageIntention
from marriageage import generateMarriageAge
from marriagedate import generateWeddingDate
from employmentstatus import generateEmploymentStatus
from income import generateIncome
from capital import generateCapital
from children import generateChildren 
from nrchildren import generateNrChildren
from birthage import generateBirthAge

#Create the class citizen
class Citizen:
    def __init__(self, ID, gender, age, birthdate, lifeexpectancyprobability, maritalstatus, marriageduration,
                 couplenr, marriageenddate, marriageintention, marriageage, marriagedate, 
                 employmentstatus, income, capital, children, nrchildren, birthage, alive, 
                 event):
        self.ID = ID
        self.gender = gender
        self.age = age
        self.birthdate = birthdate
        self.lifeexpectancyprobability = lifeexpectancyprobability
        self.maritalstatus = maritalstatus
        self.couplenr = couplenr
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
        self.alive = alive
        self.event = event

def generateBasePopulation(populationsize, baseyear, df_gender, df_age, df_lifeexpectancy, df_maritalstatus,
                           df_marriageduration, df_employmentstatus, df_incomedistribution, df_marriage, df_marriage2,
                           df_withchildren, df_nrchildren, df_birthage, df_capital):
    population = list()
    genderprobability = calculateGenderProbability(df_gender, baseyear)
    ageprobability = calculateAgeProbability(df_age, baseyear)
    marriagedurationprobability = calculateMarriageDurationProbability(df_marriageduration, baseyear)
    employmentstatusprobability = calculateEmploymentStatusProbability(df_employmentstatus, baseyear)
    incomeprobability = calculateIncomeProbability(df_incomedistribution, baseyear)
    capitalprobability = calculateCapitalProbability(df_capital, baseyear)
    marriageintentionprobability = calculateMarriageIntentionProbability(df_marriage2, baseyear)
    childrenprobability = calculateChildrenProbability(df_withchildren, baseyear)
    nrchildrenprobability = calculateNrChildrenProbability(df_nrchildren, baseyear)
    birthageprobability = calculateBirthAgeProbability(df_birthage, baseyear)
    
    for ID in range(populationsize):
        b = ("Processing citizens: " + str(ID))
        sys.stdout.write('\r'+b)
        gender = generateGender(genderprobability)
        age = generateAge(ageprobability)
        birthdate = generateBirthdate(baseyear, age)
        lifeexpectancyprobability = calculateLifeExceptancyProbability(df_lifeexpectancy, baseyear, age, gender)
        maritalstatusprobability = calculateMaritalStatusProbability(df_maritalstatus, baseyear, age)
        marriageageprobability = calculateMarriageAgeProbability(df_marriage, baseyear, gender)
        maritalstatus = generateMaritalStatus(maritalstatusprobability)
        couplenr = None
        marriageduration = generateMarriageDuration(marriagedurationprobability, maritalstatus)
        marriageenddate = generateMarriageEndDate(baseyear, maritalstatus, marriageduration)
        marriageintention = generateMarriageIntention(marriageintentionprobability)
        marriageage = generateMarriageAge(marriageageprobability, maritalstatus, marriageintention)
        marriagedate = generateWeddingDate(baseyear, marriageage, age)
        employmentstatus = generateEmploymentStatus(employmentstatusprobability, age)
        income = generateIncome(incomeprobability, age)
        capital = generateCapital(capitalprobability, age)
        children = generateChildren(childrenprobability)
        nrchildren = generateNrChildren(nrchildrenprobability, maritalstatus, age, children)
        birthage = generateBirthAge(birthageprobability, gender, age)
        alive = 1
        event = 'Created'
        population.append(Citizen(ID, gender, age, birthdate, lifeexpectancyprobability, maritalstatus, couplenr, 
                                  marriageduration, marriageenddate, marriageintention, marriageage, marriagedate, 
                                  employmentstatus, income, capital, children, nrchildren, birthage, alive, event))
    return population

