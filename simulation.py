'''
Function to run the simulation

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from datetime import datetime, timedelta
import sys

from employmentstatusprobability import calculateEmploymentStatusProbability
from incomeprobability import calculateIncomeProbability
from employmentstatuschange import changeEmploymentStatus
from maritalstatuschange import changeMaritalStatus

from ageincrease import increaseAge
from adulthood import generateAdulthood
from marriagenew import generateNewMarriage
from deceased import generateDeceased
from deceasedremove import deleteDeceased
from births import generateBirths

def runSimulation(objs, runtime, start_date, df_data, df_employmentstatus, df_income):
    print("")
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(start_date, date_format)
        
    for day in range(runtime):
        b = ("Processing date: " + str(current_date))
        sys.stdout.write('\r'+b)
        
        current_year = str(current_date)
        current_year = current_year[:4] 
        
        employmentstatusprobability = calculateEmploymentStatusProbability(df_employmentstatus, current_year)
        incomeprobability = calculateIncomeProbability(df_income, current_year)
        
        for citizen in objs:
            #Increase age on birthday
            citizen.age = increaseAge(current_date, citizen.age, citizen.birthdate)
            
            #Create a life even employment status change and income change 
            df_data, citizen = changeEmploymentStatus(current_date, citizen.age, citizen.birthdate, citizen, df_data, 
                                                      employmentstatusprobability, incomeprobability)
            
            #Create a life event adulthood
            df_data, citizen = generateAdulthood(current_date, citizen.age, citizen.birthdate, citizen, df_data)
            
            #Create a life event divorced
            df_data, citizen = changeMaritalStatus(current_date, citizen.maritalstatus, citizen.marriageenddate, citizen, df_data)
            
            #Create a life event wedding
            df_data, citizen = generateNewMarriage(current_date, citizen.maritalstatus, citizen.marriagedate, citizen, df_data)
            
            #Create a life event deceased
            df_data, citizen = generateDeceased(current_date, citizen.alive, citizen.lifeexpectancyprobability, citizen, df_data)
            
            #Delete deceased from population
            objs = deleteDeceased(objs, citizen)
            
            df_data, citizen, objs = generateBirths(current_date, citizen.birthingdate, citizen, objs, df_data)
                    
        current_date += timedelta(days=1)
    return objs, df_data

