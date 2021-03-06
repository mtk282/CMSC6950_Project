## Task 1 - Extracting argo float data in a specific region over time

#Import Python modules

import numpy as np
import pandas as pd
import argopy

##Import argo data loader

from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher()

#Load Argo data from a specific region and over a certain time frame into an x.array.Dataset

ds = argo_loader.region([-75, -45, 20, 30, 0, 10, '2001-01-01', '2006-12-31']).to_xarray()

#Create a pandas dataframe and export to a csv file

df = ds.to_dataframe()
df.to_csv (r'argopy_task1.csv', index = False, header=True)  #Export data frame to a csv file
