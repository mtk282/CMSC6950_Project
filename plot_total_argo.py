## Task 1 - Make a plot showing the temporal evoltuion (2001-2006) of total Argo float numbers for a specific region

#Import Python modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#Import Argo float csv file as a data frame and assign date column

df = pd.read_csv('argopy_task1.csv', parse_dates=[15])

#Add a year column to the dataframe

df['year'] = pd.DatetimeIndex(df['TIME']).year

#Seperate the dataframe into data frames for each year

df_2001 = df[df['TIME'].dt.year == 2001] ##Create a datframe for data collected in 2001
df_2002 = df[df['TIME'].dt.year == 2002] ##Create a datframe for data collected in 2002
df_2003 = df[df['TIME'].dt.year == 2003] ##Create a datframe for data collected in 2003
df_2004 = df[df['TIME'].dt.year == 2004] ##Create a datframe for data collected in 2004
df_2005 = df[df['TIME'].dt.year == 2005] ##Create a datframe for data collected in 2005
df_2006 = df[df['TIME'].dt.year == 2006] ##Create a datframe for data collected in 2006

##Calcuate the total number of argo floats each year

d1 = df_2001.append(df_2002) #Sequentially append dataframes together for each year until 2006
d2 = d1.append(df_2003)
d3 = d2.append(df_2004)
d4 = d3.append(df_2005)
d5 = d4.append(df_2006)

#Use geopandas to import shapefiles to be used in the subsequent plot

countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

#Define the main plotting function

def main():

    # Start the plot

    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(15,15))

    # Plot North America on each plot

    countries[countries["continent"] == "North America"].plot(ax=ax[0,0],color="black")
    countries[countries["continent"] == "North America"].plot(ax=ax[1,0],color="black")
    countries[countries["continent"] == "North America"].plot(ax=ax[2,0],color="black")
    countries[countries["continent"] == "North America"].plot(ax=ax[0,1],color="black")
    countries[countries["continent"] == "North America"].plot(ax=ax[1,1],color="black")
    countries[countries["continent"] == "North America"].plot(ax=ax[2,1],color="black")

    # Plot total number of argo floats for each year

    df_2001.plot(ax=ax[0,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", s=1)
    ax[0, 0].set_title(f'Argo Floats in 2001 (Total # of Floats = {len(df_2001)})')
    d1.plot(ax=ax[1,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", s=1)
    ax[1, 0].set_title(f'Argo Floats in 2002 (Total # of Floats = {len(d1)})')
    d2.plot(ax=ax[2,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", s=1)
    ax[2, 0].set_title(f'Argo Floats in 2003 (Total # of Floats = {len(d2)})')
    d3.plot(ax=ax[0,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", s=1)
    ax[0, 1].set_title(f'Argo Floats in 2004 (Total # of Floats = {len(d3)})')
    d4.plot(ax=ax[1,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", s=1)
    ax[1, 1].set_title(f'Argo Floats in 2005 (Total # of Floats = {len(d4)})')
    d5.plot(ax=ax[2,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", s=1)
    ax[2, 1].set_title(f'Argo Floats in 2006 (Total # of Floats = {len(d5)})')


    # Add grids and plot layout
    ax[0, 0].grid()
    ax[1, 0].grid()
    ax[2, 0].grid()
    ax[0, 1].grid()
    ax[1, 1].grid()
    ax[2, 1].grid()


    fig.tight_layout()
    plt.savefig('total_argo.png')

if __name__ == "__main__":
    main()
