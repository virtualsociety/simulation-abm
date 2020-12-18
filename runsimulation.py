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
from divorces import generateDivorces

def runSimulation(objs, runtime, start_date, df_data, df_marriage2, df_marriage, df_income,
                  df_capital, df_employmentstatus, df_marriageduration):
    warnings.filterwarnings("ignore")
    print("")
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(start_date, date_format)
    for day in range(runtime):
        b = ("Processing date: " + str(current_date))
        sys.stdout.write('\r'+b)
        
        for citizen in objs:
            #Increase age at birthday
            citizen.age = increaseAge(current_date, citizen.age, citizen.birthdate)
            
            #Reach adulthood
            df_data, citizen = generateAdulthood(current_date, citizen.age, citizen.birthdate, citizen, df_data, df_marriage2, 
                                                 df_marriage, df_income, df_capital, df_employmentstatus)
            
            #Get married
            df_data, citizen = generateNewMarriages(current_date, citizen, df_data, df_marriageduration)
            
            #End marriage
            df_data, citizen = generateDivorces(current_date, citizen, df_data)
            
        current_date += timedelta(days=1)
    return objs, df_data