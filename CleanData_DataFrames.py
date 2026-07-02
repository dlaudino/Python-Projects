import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
import os

csv_files = glob.glob(os.path.join("*.csv")) #Listing all CSV files
us_census = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True) #Concat all files
print(us_census.head())
print(us_census.dtypes) #Data Types in D.F.
print(us_census.columns) #Columns in D.F.

us_census.Income = us_census['Income'].replace('[$]','', regex=True) #Removing $ from Income column
us_census.Income = pd.to_numeric(us_census.Income) #Numeric Type

string_split = us_census['GenderPop'].str.split('_')
# Men Column
us_census['Men'] = string_split.str.get(0)
us_census.Men = us_census['Men'].replace('[M]','', regex=True) #Removing M
us_census.Men = pd.to_numeric(us_census.Men)
# Women Column
us_census['Women'] = string_split.str.get(1)
us_census.Women = us_census['Women'].replace('[F]','', regex=True) #Removing F
us_census.Women = pd.to_numeric(us_census.Women)
us_census = us_census.drop(columns='GenderPop')
us_census = us_census.drop(columns='Unnamed: 0') #Removing Column
print(us_census)

plt.scatter(us_census.Women, us_census.Men) 
plt.show()
plt.close()

# Filling Women column and removing Nan
us_census['Women'] = us_census['Women'].fillna(us_census.TotalPop - us_census.Men)
print(us_census)

duplicates = us_census.duplicated() #Analysing Duplicates
print(duplicates.value_counts())
us_census = us_census.drop_duplicates() #Dropping Duplicates
us_census = us_census.reset_index(drop=True) #Reseting Index
print(us_census)

plt.scatter(us_census.Women, us_census.Men) 
plt.show()
plt.close()

us_census.Pacific = us_census['Pacific'].replace('[%]','', regex=True) #Removing M
us_census.Pacific = pd.to_numeric(us_census.Pacific)
us_census.Asian = us_census['Asian'].replace('[%]','', regex=True) #Removing M
us_census.Asian = pd.to_numeric(us_census.Asian)
us_census.Native = us_census['Native'].replace('[%]','', regex=True) #Removing M
us_census.Native = pd.to_numeric(us_census.Native)
us_census.Black = us_census['Black'].replace('[%]','', regex=True) #Removing M
us_census.Black = pd.to_numeric(us_census.Black)
us_census.White = us_census['White'].replace('[%]','', regex=True) #Removing M
us_census.White = pd.to_numeric(us_census.White)
us_census.Hispanic = us_census['Hispanic'].replace('[%]','', regex=True) #Removing M
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)

us_census['Pacific'] = us_census['Pacific'].fillna(100 - us_census['Asian']- us_census['Native']-us_census['Black']-us_census['White']-us_census['Hispanic']) #Removing 
print(us_census)

plt.hist(us_census.Pacific,bins=50) 
plt.show()
plt.close()

plt.hist(us_census.White,bins=50) 
plt.show()
plt.close()

plt.hist(us_census.Black,bins=50) 
plt.show()
plt.close()

plt.hist(us_census.Hispanic,bins=50) 
plt.show()
plt.close()

plt.hist(us_census.Native,bins=50) 
plt.show()
plt.close()


