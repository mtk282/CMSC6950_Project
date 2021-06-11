## Task 2 - Visualzing the trajectory of an Argo float with time

#Import python libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#Import Argo float data from a csv file as data frame

df = pd.read_csv('argopy_task2.csv', parse_dates=[15]) ##Load in csv file and identify date columns

#Dataframe from geopandas used to plot countries and continents

countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

#Plot the trajectory of an Argo float

def main():

    # Start the plot - plot the trajectory of argo float
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12,8))

    # Plot Canada on the map in [0,0]

    countries[countries["name"] == "Canada"].plot(ax=ax[0,0],color="black")

    # Make four plots with different position data sets recorded since 2017

    df.plot(ax=ax[0,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="CYCLE_NUMBER", colormap="viridis", s=1)
    ax[0, 0].set_title("Argo Float Cycles since 2017 (Total # of Cycles = 131)")

    df.plot(ax=ax[1,0], x="TIME", y="LATITUDE")
    ax[1, 0].set_title("Latitude vs Time")

    df.plot(ax=ax[0,1], x="TIME", y="CYCLE_NUMBER")
    ax[0, 1].set_title("Cycle Number vs Time")

    df.plot(ax=ax[1,1], x="TIME", y="LONGITUDE")
    ax[1, 1].set_title("Longitude vs Time")


    #Add grids and plot layout
    ax[0, 0].grid()
    ax[1, 0].grid()
    ax[1, 1].grid()
    ax[0, 1].grid()

    fig.tight_layout()
    plt.savefig('argo_trajectory.png')


if __name__ == "__main__":
    main()


