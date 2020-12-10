'''
Function to calculate the
life expetancy probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateLifeExceptancyProbability(df_lifeexpectancy, baseyear, age, gender):
    df_year = df_lifeexpectancy[df_lifeexpectancy['Perioden'] == baseyear]
    probability = df_year[df_year['Leeftijd (op 31 december)'] == age]
    try:
        if gender == 'Male':
            prob = probability['Mannen'].iloc[0]
        elif gender == 'Female':
            prob = probability['Vrouwen'].iloc[0]
    except:
        prob = 1
    return prob
