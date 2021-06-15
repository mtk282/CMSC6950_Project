## Task 2 - Visualzing the trajectory of two Argo float's with time

#Import python libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#Import data from each Argo float as data frame

df_6902754 = pd.read_csv('argo_6902754.csv', parse_dates=[15]) ##Load in csv file and identify date columns
df_6902696 = pd.read_csv('argo_6902696.csv', parse_dates=[15]) ##Load in csv file and identify date columns

#Dataframe from geopandas containing shapefiles used to plot countries and continents

countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

#Plot the trajectory of two Argo floats

def main():

    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(16,12))

    # Plot Canada on the maps in [0,0] and [0,1]

    countries[countries["name"] == "Canada"].plot(ax=ax[0,0],color="black")
    countries[countries["name"] == "Canada"].plot(ax=ax[0,1],color="black")

    # Plots showing the trajectories of two argo floats and temperature variation 

    df_6902754.plot(ax=ax[0,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="CYCLE_NUMBER", colormap="viridis", s=1, figsize=(16,16))
    ax[0, 0].set_title("Argo 6902754 Cycles since deployment (Total # of Cycles = 131)")

    df_6902696.plot(ax=ax[0,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="CYCLE_NUMBER", colormap="viridis", s=1, figsize=(16,16))
    ax[0, 1].set_title("Argo 6902696 since deployment (Total # of Cycles = 160)")

    df_6902754.plot(ax=ax[1,0], x="TIME", y="LATITUDE")
    df_6902696.plot(ax=ax[1,0], x="TIME", y="LATITUDE")
    ax[1, 0].set(xlabel='Time', ylabel='Latitude')
    ax[1, 0].set_title("Latitude vs Time")
    ax[1, 0].legend(["Argo 6902754", "Argo 6902696"])

    df_6902754.plot(ax=ax[1,1], x="TIME", y="CYCLE_NUMBER")
    df_6902696.plot(ax=ax[1,1], x="TIME", y="CYCLE_NUMBER")
    ax[1, 1].set(xlabel='Time', ylabel='Cycle Number')
    ax[1, 1].set_title("Cycle Number vs Time")
    ax[1, 1].legend(["Argo 6902754", "Argo 6902696"])

    df_6902754.plot(ax=ax[2,0], x="TIME", y="LONGITUDE")
    df_6902696.plot(ax=ax[2,0], x="TIME", y="LONGITUDE")
    ax[2, 0].set(xlabel='Time', ylabel='Longitude')
    ax[2, 0].set_title("Longitude vs Time")
    ax[2, 0].legend(["Argo 6902754", "Argo 6902696"])

    df_6902754.plot(ax=ax[2,1], x="TIME", y="TEMP")
    df_6902696.plot(ax=ax[2,1], x="TIME", y="TEMP")
    ax[2, 1].set(xlabel='Time', ylabel='Temperature')
    ax[2, 1].set_title("Temperature vs Time")
    ax[2, 1].legend(["Argo 6902754", "Argo 6902696"])


    #Add grids and plot layout
    ax[0, 0].grid()
    ax[1, 0].grid()
    ax[1, 1].grid()
    ax[0, 1].grid()
    ax[2, 0].grid()
    ax[2, 1].grid()
    fig.tight_layout()
    plt.savefig('argo_trajectory.png')


if __name__ == "__main__":
    main()


