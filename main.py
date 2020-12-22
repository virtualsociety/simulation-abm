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
from couplenr import generateCouplenrs
from basepopulationdataframe import generateDataframeBasePopulation
from runtime import generateRuntime
from runsimulation import runSimulation

#Read the input files
df_gender = pd.read_csv('./Input_2/Bevolking__kerncijfers_07122020_100024.csv', delimiter = ';')
df_age = pd.read_csv('./Input_2/Bevolking__kerncijfers_07122020_112736.csv', delimiter = ';')
df_lifeexpextancy = pd.read_csv('./Input_2/Levensverwachting__geslacht__leeftijd__per_jaar_en_periode_van_vijf_jaren__07122020_120956.csv', delimiter = ';')
df_maritalstatus = pd.read_csv('./Input_2/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_08122020_110015.csv', delimiter = ';')
df_marriageduration = pd.read_csv('./Input_2/Bestaande_huwelijken_en_partnerschappen__relatieduur__1_januari_08122020_121148.csv', delimiter = ';')
df_employmentstatus = pd.read_csv('./Input_2/Arbeidsdeelname__kerncijfers__08122020_130106.csv', delimiter = ';')
df_income = pd.read_csv('./Input_2/Inkomen_van_personen__inkomensklassen__persoonskenmerken_09122020_094158.csv', delimiter = ';')
df_marriage = pd.read_csv('./Input_2/Huwen_en_huwelijksontbinding__geslacht__leeftijd__31_december___regio_11122020_100116.csv', delimiter = ';')
df_marriage2 = pd.read_csv('./Input_2/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_11122020_105220.csv', delimiter = ';')
df_withchildren =  pd.read_csv('./Input_2/Particuliere_huishoudens_naar_samenstelling_en_grootte__1_januari_14122020_114929.csv', delimiter = ';')
df_nrchildren = pd.read_csv('./Input_2/Huishoudens__kindertal__leeftijdsklasse_kind__regio__1_januari_14122020_114332.csv', delimiter = ';')
df_birthage =  pd.read_csv('./Input_2/Levend_geboren_kinderen__migratieachtergrond_moeder_en_leeftijd_moeder_14122020_112329.csv', delimiter = ';')
df_capital = pd.read_csv('./Input_2/vermogensklassen.csv', delimiter = ';')

#Initialize main variables
start_date = '2011-01-01' #Set the start date of the simulation
end_date = '2011-12-31' #Set the end data of the simulation
baseyear = int(start_date[:4])

#Set the scalar
scalar = 1000

#Set the pickle
pickle = 'Y'

#Construct or load the base population
if pickle == 'Y':
    print('Loading base population')
    dill.load_session('population.pkl')
else:
    print('Determining base population')
    populationsize = int(calculateBasePopulationSize(df_gender, baseyear, scalar))
    population = generateBasePopulation(populationsize, baseyear, df_gender, df_age, df_lifeexpextancy, df_maritalstatus, df_marriageduration,
                                        df_employmentstatus, df_income, df_marriage, df_marriage2, df_withchildren, df_nrchildren,
                                        df_birthage, df_capital)
    print("")
    print('Creating couples')
    population = generateCouplenrs(population)
    dill.dump_session('population.pkl') 
    
#Process the data basepopulation
df_data_base = generateDataframeBasePopulation(population, start_date)
df_data_base.to_csv('basepopulation.csv') 

#Run the simulation
runtime =generateRuntime(start_date, end_date)
population, df_data_simulated = runSimulation(population, runtime, start_date, df_data_base, df_marriage2, df_marriage, df_income, df_capital, 
                                              df_employmentstatus, df_marriageduration)
df_data_simulated = df_data_simulated.sort_values(by=['ID', 'Mutation date'])
df_data_simulated.to_csv('simulatedpopulation.csv') 