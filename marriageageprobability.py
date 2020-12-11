'''
Function to calculate the marriage age probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateMarriageAgeProbability(df_marriage, baseyear, gender):
    year = str(baseyear)
    df_marriageageprobability = df_marriage[year]
    marriageageprobability = list()
    if gender == 'Male':
        for i in range (0,11):
            marriageageprobability.append(df_marriageageprobability.iloc[i])
    elif gender == 'Female':
        for i in range (11, 22):
            marriageageprobability.append(df_marriageageprobability.iloc[i])
    return marriageageprobability
