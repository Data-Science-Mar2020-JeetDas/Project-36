# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/Project-36.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project - 36 : Ill-defined causes in cause-of-death registration (%)");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

country = df.groupby(['Location'])[['Period']].count()
print("---------------------------------")
print("\tAvailable country names : ")
print("-------------------------------")
print(country)
print("-------------------------------")
count = 0
for row in range(len(country)): 
        count = count+1
print("total no. of country = ",count)        
print("-----------------------------\n")


# Question - D : Available years data for which data is available

years = df.groupby(['Period'])[['Location']].count()
print("---------------------------------")
print("\tAvailable years data : ")
print("-------------------------------")
print(years)
print("-------------------------------")
count = 0
for row in range(len(years)): 
        count = count+1
print("total no. of years = ",count)        
print("-----------------------------\n")



# Question - E :Types of available indicators

indicator = df.groupby(['Indicator'])[['Period']].count()
print("---------------------------------")
print("\tAvailable types of indicators : ")
print("-------------------------------")
print(indicator)
print("-------------------------------")
count = 0
for row in range(len(indicator)): 
        count = count+1
print("total no. of indicators = ",count)        
print("-----------------------------\n")

#******************* Question - : 2007/2008/2009 :  ********************


df2007 = df[df.Period == 2007]
print("\n\n--------------[ OUTPUT for 2007 ]----------------------\n\n")
print(df2007[['Location','Period','First Tooltip']])

df2008 = df[df.Period == 2008]
print("\n\n--------------[ OUTPUT for 2008 ]----------------------\n\n")
print(df2008[['Location','Period','First Tooltip']])

df2009 = df[df.Period == 2009]
print("\n\n--------------[ OUTPUT for 2009 ]----------------------\n\n")
print(df2009[['Location','Period','First Tooltip']])

i = np.arange(len(df2007['Location']))
print(i)

i1 = np.arange(len(df2008['Location']))
print(i1)

i2 = np.arange(len(df2009['Location']))
print(i2)

#--------------- plot for 2007/2008/2009 ----------------------

plt.title('Question - : plot for 2007/2008/2009')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df2007['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2007")

plt.plot(i1,df2008['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2008")

plt.plot(i2,df2009['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2009")

plt.legend()
plt.show()


#******************* Question - : 2010/2011/2012 :  ********************


df2010 = df[df.Period == 2010]
print("\n\n--------------[ OUTPUT for 2010 ]----------------------\n\n")
print(df2010[['Location','Period','First Tooltip']])

df2011 = df[df.Period == 2011]
print("\n\n--------------[ OUTPUT for 2011 ]----------------------\n\n")
print(df2011[['Location','Period','First Tooltip']])

df2012 = df[df.Period == 2012]
print("\n\n--------------[ OUTPUT for 2012 ]----------------------\n\n")
print(df2012[['Location','Period','First Tooltip']])

i = np.arange(len(df2010['Location']))
print(i)

i1 = np.arange(len(df2011['Location']))
print(i1)

i2 = np.arange(len(df2012['Location']))
print(i2)

#--------------- plot for 2010/2011/2012 ----------------------

plt.title('Question - : plot for 2010/2011/2012')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df2010['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2010")

plt.plot(i1,df2011['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011")

plt.plot(i2,df2012['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2012")

plt.legend()
plt.show()


#******************* Question - : 2013/2014/2015/2016 :  ********************


df2013 = df[df.Period == 2013]
print("\n\n--------------[ OUTPUT for 2013 ]----------------------\n\n")
print(df2013[['Location','Period','First Tooltip']])

df2014 = df[df.Period == 2014]
print("\n\n--------------[ OUTPUT for 2014 ]----------------------\n\n")
print(df2014[['Location','Period','First Tooltip']])

df2015 = df[df.Period == 2015]
print("\n\n--------------[ OUTPUT for 2015 ]----------------------\n\n")
print(df2015[['Location','Period','First Tooltip']])

df2016 = df[df.Period == 2016]
print("\n\n--------------[ OUTPUT for 2016 ]----------------------\n\n")
print(df2016[['Location','Period','First Tooltip']])

i = np.arange(len(df2013['Location']))
print(i)

i1 = np.arange(len(df2014['Location']))
print(i1)

i2 = np.arange(len(df2015['Location']))
print(i2)

i3 = np.arange(len(df2016['Location']))
print(i3)

#--------------- plot for 2013/2014/2015/2016 ----------------------

plt.title('Question - : plot for 2013/2014/2015/2016')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df2013['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2013")

plt.plot(i1,df2014['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2014")

plt.plot(i2,df2015['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2015")

plt.plot(i3,df2016['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2016")


plt.legend()
plt.show()

