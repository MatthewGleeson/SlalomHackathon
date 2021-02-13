import numpy as np
import pandas as pd
#np.loadtxt(open("myfile.csv", "rb"), delimiter=",")



df = pd.read_csv('myfile.csv')

df.drop_duplicates()

myNumpyArray = df.iloc[:,0].apply(hash)

myNumpyArray.to_numpy()



#toHash  = df[:,1]


print(df.head)


df.iloc[0].apply(hash)
#myMatrix = np.genfromtxt('myfile.csv',dtype='str')
#print(myMatrix[0])