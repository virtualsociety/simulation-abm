'''
Function to create new citizerns

By Dr. Raymond Hoogendoorn
Copyright 2021
'''

from lifeexpectancyprobability import calculateLifeExceptancyProbability
from genderprobability import calculateGenderProbability
from maritalstatusprobability import calculateMaritalStatusProbability
from marriagedurationprobability import calculateMarriageDurationProbability
from maritalstatus import generateMaritalStatus

from gender import generateGender

#Create the class citizen
class Citizen:
    def __init__(self, ID, gender, age, birthdate, lifeexpectancyprobability, maritalstatus, marriageduration,
                 couplenr, marriageenddate, marriageintention, marriageage, marriagedate, 
                 employmentstatus, income, capital, children, nrchildren, birthage, birthingdate,
                 alive, event):
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
        self.birthingdate = birthingdate
        self.alive = alive
        self.event = event
        
def generateCitizen(objs, df, currentdate, df_lifeexpectancy, df_gender, df_maritalstatus):
    currentdate = str(currentdate)
    currentyear = str(currentdate)
    currentdate = currentdate[:10]
    currentyear = currentyear[:4]
    genderprobability = calculateGenderProbability(df_gender, currentyear)
    ID = max(df['ID']) + 1
    gender = generateGender(genderprobability)
    age = 0
    birthdate = currentdate
    lifeexpectancyprobability = calculateLifeExceptancyProbability(df_lifeexpectancy, currentyear, 1, gender)
    maritalstatusprobability = calculateMaritalStatusProbability(df_maritalstatus, currentyear, 1)
    maritalstatus = generateMaritalStatus(maritalstatusprobability)
    couplenr = int(0)
    marriageduration = ""
    marriageenddate= ""
    marriageintention = 'No'
    marriageage = ""
    marriagedate = ""
    employmentstatus = 'Child'
    income = 0
    capital = 0
    children = 'No'
    nrchildren = 0
    birthage = ""
    birthingdate = ""
    alive = 1
    event = 'Life event: Birth'
    citizen = Citizen(ID, gender, age, birthdate, lifeexpectancyprobability, maritalstatus, couplenr, 
                      marriageduration, marriageenddate, marriageintention, marriageage, marriagedate, 
                      employmentstatus, income, capital, children, nrchildren, birthage, birthingdate, 
                      alive, event)
    
    mutationdate = str(currentdate)
    mutationdate = mutationdate[:10]
    
    new_event = {'Mutation date': mutationdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                 'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                 'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                 'Couple nr': citizen.couplenr, 'Marriage duration': citizen.marriageduration, 
                 'Marriage end date': citizen.marriageenddate, 'Marriage intention': citizen.marriageintention, 
                 'Marriage age': citizen.marriageage, 'Wedding date': citizen.marriagedate, 
                 'Children': citizen.children, 'Employment status': citizen.employmentstatus, 'Income': citizen.income, 
                 'Capital': citizen.capital, 'NrChildren': citizen.nrchildren, 'Birth age': citizen.birthage, 
                 'Birthing date': citizen.birthingdate, 'Alive': citizen.alive, 'Event': citizen.event}
        
    df = df.append(new_event, ignore_index=True)
    
    objs.append(citizen)
    
    return objs, df

