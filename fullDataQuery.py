import pandas as pd



#Parameters: EIN
#Requires: fulldata.csv- csv file full of data extracted from 990 forms
#Description: Function takes in EIN, spits out url, phone number, name based on 
def fullDataQuery(EIN):
    df = pd.read_csv('fulldata.csv')
    #df.drop_duplicates()

    s = df.loc[df['EIN'] == EIN]

    print(s)

    if 'URL' in s.index:
        websiteColumn = s.loc['URL']
        website = websiteColumn.loc[websiteColumn.first_valid_index()]
    else:
        website = ''
    
    if 'Phone' in s.index:
        phoneColumn = s.loc['Phone']
        phone = phoneColumn.loc[phoneColumn.first_valid_index()]
    else:
        phone = ''

    if 'STREET' in s.index:
        addressColumn = s.loc['STREET']
        address = addressColumn.loc[addressColumn.first_valid_index()]
    else:
        address = ''

    toReturn = {'website': website, 'phone':phone, 'address':address}

    return toReturn




