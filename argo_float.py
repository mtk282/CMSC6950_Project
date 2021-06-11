## Task 2 - Extract data from a single Argo float since its deployment

#Python modules

import numpy as np
import pandas as pd
import argopy

#Argo data loader

from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher()

#Extract data from a Argo float # 6902754

ds = argo_loader.float(6902754).to_xarray()

#Create a pandas dataframe and export as a csv file

df = ds.to_dataframe() ##Covert data to a pandas dataframe
df.to_csv (r'argopy_task2.csv', index = False, header=True)  ##Export data to a csv file
