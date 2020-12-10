'''
Population simulation 
to create synthetic data
By Dr. Raymond Hoogendoorn
Copyright 2020
'''
#Import the modules
import pandas as pd
import dill

from basepopulationsize import calculateBasePopulationSize
from basepopulation import generateBasePopulation
from basepopulationdataframe import generateDataframeBasePopulation
from runtime import generateRuntime
from simulation import runSimulation

#Read the input files
df_gender = pd.read_csv('../input_2/Bevolking__kerncijfers_07122020_100024.csv', delimiter = ';')
df_age = pd.read_csv('../input_2/Bevolking__kerncijfers_07122020_112736.csv', delimiter = ';')
df_lifeexpextancy = pd.read_csv('../input_2/Levensverwachting__geslacht__leeftijd__per_jaar_en_periode_van_vijf_jaren__07122020_120956.csv', delimiter = ';')
df_maritalstatus = pd.read_csv('../input_2/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_08122020_110015.csv', delimiter = ';')
df_marriageduration = pd.read_csv('../input_2/Bestaande_huwelijken_en_partnerschappen__relatieduur__1_januari_08122020_121148.csv', delimiter = ';')
df_employmentstatus = pd.read_csv('../input_2/Arbeidsdeelname__kerncijfers__08122020_130106.csv', delimiter = ';')
df_incomedistribution = pd.read_csv('../input_2/Inkomen_van_personen__inkomensklassen__persoonskenmerken_09122020_094158.csv', delimiter = ';')

#Initialize main variables
start_date = '2011-01-01' #Set the start date of the simulation
end_date = '2011-12-31' #Set the end data of the simulation
baseyear = int(start_date[:4])

#set the scalar
scalar = 1000

#Set the pickle
pickle = 'N'

#Construct or load the base population
if pickle == 'Y':
    print('Loading base population')
    dill.load_session('population.pkl')
else:
    print('Determining base population')
    populationsize = int(calculateBasePopulationSize(df_gender, baseyear, scalar))
    population = generateBasePopulation(populationsize, baseyear, df_gender, df_age, df_lifeexpextancy, df_maritalstatus, df_marriageduration,
                                        df_employmentstatus, df_incomedistribution)
    dill.dump_session('population.pkl') 
    
#Print the data
#for citizen in population:
#    print('ID: {}, Gender: {}, Age: {}, Birthdate: {}, Life expectancy prob: {}, Marital status: {}, Marriage duration: {}, Marriage end date: {}, Employment status: {}, Income: {}, Event: {}'.format(citizen.ID, citizen.gender, citizen.age, citizen.birthdate, citizen.lifeexpectancyprobability, citizen.maritalstatus, citizen.marriageduration, citizen.marriageenddate, citizen.employmentstatus, citizen.income, citizen.event))  

#Process the data basepopulation
df_data_base = generateDataframeBasePopulation(population, start_date)
df_data_base.to_csv('basepopulation.csv') 

#Run the simulation
runtime = generateRuntime(start_date, end_date)
population, df_data_simulation = runSimulation(population, runtime, start_date, df_data_base, df_employmentstatus)

#Sort the dataframe by ID
df_data_simulation = df_data_simulation.sort_values(by=['ID'])
df_data_simulation.to_csv('simulatedpopulation.csv') 