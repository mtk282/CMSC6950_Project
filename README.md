## CMSC 6950 Project - Spring 2021

Course project for CMSC 6950

Michael King

Project title: argopy (https://argopy.readthedocs.io/en/latest/index.html)

## Software Setup

Assuming you already have a conda installation such as Miniforge installed,


    conda create -n argopy
    conda activate argopy
    conda install xarray fsspec scikit-learn erddapy gsw aiohttp netCDF4 dask toolz
    conda install ipython ipywidgets tqdm matplotlib cartopy seaborn
    conda install numpy pandas geopandas
    conda install -c conda-forge argopy

## Using argopy



## Computational Tasks

Task 1 - Change in the total number of Argo floats for an area of interest within a certain time frame.

Task 2 - Trajectory of an Argo float through time since its deployment

