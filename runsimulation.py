'''
Function to run the simulation

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from datetime import datetime, timedelta
import sys
import warnings

from ageincrease import increaseAge
from adulthood import generateAdulthood
from marriagesnew import generateNewMarriages
from childrennew import generateNewChildren
from divorces import generateDivorces
from retired import generateRetired
from deceased import generateDeceased
from widow import generateWidows
from deceaseddelete import deleteDeceased

def runSimulation(objs, runtime, start_date, df_data, df_marriage2, df_marriage, df_income,
                  df_capital, df_employmentstatus, df_marriageduration, df_nrchildren,
                  df_births, scalar, df_gender, df_lifeexpectancy, df_maritalstatus):
    warnings.filterwarnings("ignore")
    print("")
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(start_date, date_format)
    for day in range(runtime):
        b = ("Processing date: " + str(current_date))
        sys.stdout.write('\r'+b)
        
        for citizen in objs:
            #Increase age at birthday
            citizen.age = increaseAge(current_date, citizen.age, citizen.birthdate, citizen)
            
            #Reach adulthood
            df_data, citizen = generateAdulthood(current_date, citizen.age, citizen.birthdate, citizen, df_data, df_marriage2, 
                                                 df_marriage, df_income, df_capital, df_employmentstatus)
            
            #Get married
            df_data, citizen = generateNewMarriages(current_date, citizen, df_data, df_marriageduration, objs)
            
            #Create children for citizen
            df_data, citizen, objs = generateNewChildren(current_date, citizen, df_data, df_nrchildren, objs,
                                                         df_lifeexpectancy, df_gender, df_maritalstatus)
            
            #End marriage
            df_data, citizen = generateDivorces(current_date, citizen, df_data)
            
            #Retired
            df_data, citizen = generateRetired(current_date, citizen, df_data)
            
            #Deceased
            df_data, citizen =  generateDeceased (current_date, citizen, df_data)
            
            #Change marital status partner deceased
            df_data, objs = generateWidows (current_date, citizen, objs, df_data)
            
            #Delete deceased from list
            objs = deleteDeceased(citizen, objs)
                    
        current_date += timedelta(days=1)
        
    return objs, df_data