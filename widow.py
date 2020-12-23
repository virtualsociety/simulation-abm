'''
Function to generate changes in marital status after
partner is deceased

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def generateWidows(currentdate, citizen, objs, df):
    if citizen.alive == 0:
        for citizen_partner in objs:
            if citizen_partner.couplenr == citizen.couplenr and citizen_partner.gender != citizen.gender and citizen_partner.maritalstatus == 'Married':
                citizen_partner.maritalstatus = 'Widowed'
                citizen_partner.event = 'Life event: Widowed'
                mutationdate = str(currentdate)
                mutationdate = mutationdate[:10]
        
                new_event = {'Mutation date': mutationdate, 'ID': citizen_partner.ID, 'Gender': citizen_partner.gender,
                             'Age': citizen_partner.age, 'Birthdate': citizen_partner.birthdate, 
                             'Life expectancy': citizen_partner.lifeexpectancyprobability, 'Marital status': citizen_partner.maritalstatus,
                             'Couple nr': citizen_partner.couplenr, 'Marriage duration': citizen_partner.marriageduration, 
                             'Marriage end date': citizen_partner.marriageenddate, 'Marriage intention': citizen_partner.marriageintention, 
                             'Marriage age': citizen_partner.marriageage, 'Wedding date': citizen_partner.marriagedate, 
                             'Children': citizen_partner.children, 'Employment status': citizen_partner.employmentstatus, 'Income': citizen_partner.income, 
                             'Capital': citizen_partner.capital, 'NrChildren': citizen_partner.nrchildren, 'Birth age': citizen_partner.birthage, 
                             'Birthing date': citizen_partner.birthingdate, 'Alive': citizen_partner.alive, 'Event': citizen_partner.event}
                
                df = df.append(new_event, ignore_index=True)
    return df, objs