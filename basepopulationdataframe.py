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
    couplenrlist = list()
    marriagedurationlist = list()
    marriageenddatelist = list()
    marriageintentionlist = list()
    marriageagelist = list()
    marriagedatelist = list()
    employmentstatuslist = list()
    incomelist = list()
    capitallist = list()
    childrenlist = list()
    nrchildrenlist = list()
    birthagelist = list()
    birthingdatelist = list()
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
        couplenrlist.append(citizen.couplenr)
        marriagedurationlist.append(citizen.marriageduration)
        marriageenddatelist.append(citizen.marriageenddate)
        marriageintentionlist.append(citizen.marriageintention)
        marriageagelist.append(citizen.marriageage)
        marriagedatelist.append(citizen.marriagedate)
        employmentstatuslist.append(citizen.employmentstatus)
        incomelist.append(citizen.income)
        capitallist.append(citizen.capital)
        childrenlist.append(citizen.children)
        nrchildrenlist.append(citizen.nrchildren)
        birthagelist.append(citizen.birthage)
        birthingdatelist.append(citizen.birthingdate)
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
    df['Couple nr'] = couplenrlist
    df['Marriage duration'] = marriagedurationlist
    df['Marriage end date'] = marriageenddatelist
    df['Marriage intention'] = marriageintentionlist
    df['Marriage age'] = marriageagelist
    df['Wedding date'] = marriagedatelist
    df['Employment status'] = employmentstatuslist
    df['Income'] = incomelist
    df['Capital'] = capitallist
    df['Children'] = childrenlist
    df['NrChildren'] = nrchildrenlist
    df['Birth age'] = birthagelist
    df['Birthing date'] = birthingdatelist
    df['Alive'] = alivelist
    df['Event'] = eventlist
    return df
    



