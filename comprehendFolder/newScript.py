import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize

#np.loadtxt(open("myfile.csv", "rb"), delimiter=",")



df = pd.read_csv('myfile2-1.csv')

df.drop_duplicates()



with open('categories.json') as json_file:
    jsonData = json.load(json_file)

json_normalize(jsonData)

df = pd.DataFrame.from_dict(jsonData, orient='columns')






myNumpyArray = df.iloc[:,0].apply(hash)

myNumpyArray.to_numpy()


#toHash  = df[:,1]


print(df.head)


df.iloc[0].apply(hash)
#myMatrix = np.genfromtxt('myfile.csv',dtype='str')
#print(myMatrix[0])