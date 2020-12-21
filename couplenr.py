'''
Function to create couplenrs

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def generateCouplenrs(objs):
    couple_male = 1
    couple_female = 1
    for citizen in objs:
        if citizen.gender == 'Male' and citizen.maritalstatus == 'Married' and citizen.alive == 1:
            citizen.couplenr = couple_male
            couple_male += 1
        elif citizen.gender == 'Female' and citizen.maritalstatus == 'Married' and citizen.alive == 1:
            citizen.couplenr = couple_female
            couple_female += 1
    
    for citizen_female in objs:
        if citizen_female.gender == 'Female' and citizen_female.couplenr > 0 and citizen_female.alive == 1:
            for citizen_male in objs:
                if citizen_female.couplenr == citizen_male.couplenr:
                    citizen_male.marriageduration = citizen_female.marriageduration
                    citizen_male.marriageenddate = citizen_female.marriageenddate
                    citizen_male.children = citizen_female.children
                    citizen_male.nrchildren = citizen_female.nrchildren
                
    return objs

        