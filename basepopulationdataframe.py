'''
Function to create the dateframe
of the basepopulation

By Dr. Raymond Hoogendoorn
Copyright 2020
'''
import pandas as pd

def generateDataframeBasePopulation(objs, startdate):
    datelist = list()
    idlist = list()
    genderlist = list()
    agelist = list()
    birthdatelist = list()
    lifeexpectancylist = list()
    maritalstatuslist = list()
    marriagedurationlist = list()
    marriageenddatelist = list()
    employmentstatuslist = list()
    incomelist = list()
    alivelist = list()
    eventlist = list()
    for citizen in objs:
        datelist.append(startdate)
        idlist.append(citizen.ID)
        genderlist.append(citizen.gender)
        agelist.append(citizen.age)
        birthdatelist.append(citizen.birthdate)
        lifeexpectancylist.append(citizen.lifeexpectancyprobability)
        maritalstatuslist.append(citizen.maritalstatus)
        marriagedurationlist.append(citizen.marriageduration)
        marriageenddatelist.append(citizen.marriageenddate)
        employmentstatuslist.append(citizen.employmentstatus)
        incomelist.append(citizen.income)
        alivelist.append(citizen.alive)
        eventlist.append(citizen.event)
    df = pd.DataFrame()
    df['Mutation date'] = datelist
    df['ID'] = idlist
    df['Gender'] = genderlist
    df['Age'] = agelist
    df['Birthdate'] = birthdatelist
    df['Life expectancy'] = lifeexpectancylist
    df['Marital status'] = maritalstatuslist
    df['Marriage duration'] = marriagedurationlist
    df['Marriage end date'] = marriageenddatelist
    df['Employment status'] = employmentstatuslist
    df['Income'] = incomelist
    df['Alive'] = alivelist
    df['Event'] = eventlist
    return df
    



