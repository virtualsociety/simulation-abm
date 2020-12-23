'''
Function to generate the life event of
entering into adulthood

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from marriageintentionprobability import calculateMarriageIntentionProbability
from marriageintention import generateMarriageIntention
from marriageageprobability  import calculateMarriageAgeProbability
from marriageage import generateMarriageAge
from marriagedate import generateWeddingDate
from incomeprobability import calculateIncomeProbability
from income import generateIncome
from employmentstatusprobability import calculateEmploymentStatusProbability
from employmentstatus import generateEmploymentStatus
from capitalprobability import calculateCapitalProbability
from capital import generateCapital


def generateAdulthood(currentdate, age, birthdate, citizen, df, df_marriage2, df_marriage, 
                      df_income, df_capital, df_employmentstatus):
    currentday = str(currentdate)
    currentyear = currentday[:4]
    birthday = str(birthdate)
    currentday = currentday[5:10]
    birthday = birthday[5:10]
    
    if currentday == birthday and age == 18 and citizen.alive == 1:
        citizen.event = 'Life event: Adulthood'
        mutationdate = str(currentdate)
        mutationdate = mutationdate[:10]
        
        marriageintentionprobability = calculateMarriageIntentionProbability(df_marriage2, currentyear)
        citizen.marriageintention = generateMarriageIntention(marriageintentionprobability)

        marriageageprobability = calculateMarriageAgeProbability(df_marriage, currentyear, citizen.gender)
        citizen.marriageage = generateMarriageAge(marriageageprobability, citizen.maritalstatus, citizen.marriageintention)
        
        citizen.marriagedate = generateWeddingDate(currentyear, citizen.marriageage, citizen.age)
        
        incomeprobability = calculateIncomeProbability(df_income, currentyear)
        citizen.income =  generateIncome(incomeprobability, citizen.age)
        
        employmentstatusprobability = calculateEmploymentStatusProbability(df_employmentstatus, currentyear)
        citizen.employmentstatus = generateEmploymentStatus(employmentstatusprobability, citizen.age)
        
        capitalprobability = calculateCapitalProbability(df_capital, currentyear)
        citizen.capital = generateCapital(capitalprobability, citizen.age)
        
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
    return df, citizen
        