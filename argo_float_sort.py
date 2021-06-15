##Task 2 - Import argopy_task2.csv and seperate 2 Argo floats into two dataframes and them export as csv files

#Import python libraries

import numpy as np
import pandas as pd

#Import Argo float data from a csv file as dataframe

df = pd.read_csv('argopy_task2.csv', parse_dates=[15]) ##Load in csv file and identify date columns

#Make two dataframes - one for each Argo platform number

df_6902754 = df[df.PLATFORM_NUMBER == 6902754]
df_6902696 = df[df.PLATFORM_NUMBER == 6902696]

#Export Argo dataframes to csv files

df_6902754.to_csv (r'argo_6902754.csv', index = False, header=True)
df_6902696.to_csv (r'argo_6902696.csv', index = False, header=True)
