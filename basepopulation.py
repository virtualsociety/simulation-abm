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
from employmentstatusprobability import calculateEmploymentStatusProbability
from incomeprobability import calculateIncomeProbability
from gender import generateGender
from age import generateAge
from birthdate import generateBirthdate
from maritalstatus import generateMaritalStatus
from marriageduration import generateMarriageDuration
from marriageenddate import generateMarriageEndDate
from employmentstatus import generateEmploymentStatus
from income import generateIncome


#Create the class citizen
class Citizen:
    def __init__(self, ID, gender, age, birthdate, lifeexpectancyprobability, maritalstatus, marriageduration,
                 marriageenddate, employmentstatus, income, alive, event):
        self.ID = ID
        self.gender = gender
        self.age = age
        self.birthdate = birthdate
        self.lifeexpectancyprobability = lifeexpectancyprobability
        self.maritalstatus = maritalstatus
        self.marriageduration = marriageduration
        self.marriageenddate = marriageenddate
        self.employmentstatus = employmentstatus
        self.income = income
        self.alive = alive
        self.event = event

def generateBasePopulation(populationsize, baseyear, df_gender, df_age, df_lifeexpectancy, df_maritalstatus,
                           df_marriageduration, df_employmentstatus, df_incomedistribution):
    population = list()
    genderprobability = calculateGenderProbability(df_gender, baseyear)
    ageprobability = calculateAgeProbability(df_age, baseyear)
    marriagedurationprobability = calculateMarriageDurationProbability(df_marriageduration, baseyear)
    employmentstatusprobability = calculateEmploymentStatusProbability(df_employmentstatus, baseyear)
    incomeprobability = calculateIncomeProbability(df_incomedistribution, baseyear)
    
    for ID in range(populationsize):
        b = ("Processing citizens: " + str(ID))
        sys.stdout.write('\r'+b)
        gender = generateGender(genderprobability)
        age = generateAge(ageprobability)
        birthdate = generateBirthdate(baseyear, age)
        lifeexpectancyprobability = calculateLifeExceptancyProbability(df_lifeexpectancy, baseyear, age, gender)
        maritalstatusprobability = calculateMaritalStatusProbability(df_maritalstatus, baseyear, age)
        maritalstatus = generateMaritalStatus(maritalstatusprobability)
        marriageduration = generateMarriageDuration(marriagedurationprobability, maritalstatus)
        marriageenddate = generateMarriageEndDate(baseyear, maritalstatus, marriageduration)
        employmentstatus = generateEmploymentStatus(employmentstatusprobability, age)
        income = generateIncome(incomeprobability, age)
        alive = 1
        event = 'Created'
        population.append(Citizen(ID, gender, age, birthdate, lifeexpectancyprobability, maritalstatus, marriageduration,
                                  marriageenddate, employmentstatus, income, alive, event))
    return population 