'''
Function to run the simulation

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from datetime import datetime, timedelta
import sys

from employmentstatusprobability import calculateEmploymentStatusProbability
from employmentstatuschange import changeEmploymentStatus

from ageincrease import increaseAge
from adulthood import generateAdulthood

def runSimulation(objs, runtime, start_date, df_data, df_employmentstatus):
    print("")
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(start_date, date_format)
        
    for day in range(runtime):
        b = ("Processing date: " + str(current_date))
        sys.stdout.write('\r'+b)
        
        current_year = str(current_date)
        current_year = current_year[:4]
        
        employmentstatusprobability = calculateEmploymentStatusProbability(df_employmentstatus, current_year)
        
        for citizen in objs:
            #Increase age on birthday
            citizen.age = increaseAge(current_date, citizen.age, citizen.birthdate)
            #Change the employment status when turning 15 and create life event
            df_data, citizen = changeEmploymentStatus(current_date, citizen.age, citizen.birthdate, citizen, df_data, employmentstatusprobability)
            
            #Create a life event adulthood
            df_data, citizen = generateAdulthood(current_date, citizen.age, citizen.birthdate, citizen, df_data)
                    
        current_date += timedelta(days=1)
    return objs, df_data

