## Task 2 - Extract data from two Argo floats since deployment

#Python modules

import numpy as np
import pandas as pd
import argopy

# Define Argo data loader used to load Argo data

from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher()

#Extract data from Argo floats 6902754 and 6902696

ds = argo_loader.float([6902754, 6902696]).to_xarray() 
print(ds)

#Create a pandas dataframe and export as a csv file

df = ds.to_dataframe() ##Covert data to a pandas dataframe
df.to_csv (r'argopy_task2.csv', index = False, header=True)  ##Export data to a csv file
