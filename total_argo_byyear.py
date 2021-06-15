## Task 1 Continued - Seperate Argo float data into dataframes for each year

#Import Python modules

import numpy as np
import pandas as pd

#Import Argo float csv file as a data frame and assign date column

df = pd.read_csv('argopy_task1.csv', parse_dates=[15])

#Add a year column to the dataframe

df['year'] = pd.DatetimeIndex(df['TIME']).year

#Seperate the dataframe into data frames for each year

df_2001 = df[df['TIME'].dt.year == 2001] ##Create a dataframe for data collected in 2001
df_2002 = df[df['TIME'].dt.year == 2002] ##Create a dataframe for data collected in 2002
df_2003 = df[df['TIME'].dt.year == 2003] ##Create a dataframe for data collected in 2003
df_2004 = df[df['TIME'].dt.year == 2004] ##Create a dataframe for data collected in 2004
df_2005 = df[df['TIME'].dt.year == 2005] ##Create a dataframe for data collected in 2005
df_2006 = df[df['TIME'].dt.year == 2006] ##Create a dataframe for data collected in 2006

##Calcuate the total number of argo floats each year

d1 = df_2001.append(df_2002) #Sequentially append dataframes together
d2 = d1.append(df_2003) # 2001-2003
d3 = d2.append(df_2004) # 2001-2004
d4 = d3.append(df_2005) # 2001-2005
d5 = d4.append(df_2006) # 2001-2006

#Export each data frame to a csv file

df_2001.to_csv (r'total_argo_2001.csv', index = False, header=True)
d1.to_csv (r'total_argo_2002.csv', index = False, header=True)
d2.to_csv (r'total_argo_2003.csv', index = False, header=True)
d3.to_csv (r'total_argo_2004.csv', index = False, header=True)
d4.to_csv (r'total_argo_2005.csv', index = False, header=True)
d5.to_csv (r'total_argo_2006.csv', index = False, header=True)
