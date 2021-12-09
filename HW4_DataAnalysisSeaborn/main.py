# Name:Alejandra Hernandez
# Date:10/01/2020
# Program:HW4_DataAnalysisSeaborn.py
# Desc: Display usage of Seaborn library

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    tips = pd.read_csv(
        "C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW4_DataAnalysisSeaborn\\workerstips.csv")
    # A)
    aData = sns.stripplot(x='total_bill', y='tip', data=tips)
    plt.show()

    # B)
    myGraph = sns.stripplot(x='total_bill', y='tip', hue='smoker', marker='*', data=tips)
    plt.rcParams['figure.figsize'] = (10, 300)
    plt.show()

    #C)
    sns.barplot(x='day', y='tip',  data=tips)
    plt.show()
    print("Sunday has the highest average tip.")
    print()

    #D)
    sns.barplot(x='day', y='tip',hue='time', data=tips)
    plt.show()
    print("During the weekend there were no lunch tips.")
    print()

    #E)
    flight = pd.read_csv(
        "C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW4_DataAnalysisSeaborn\\flightsData.csv")
    sns.lineplot(x='year',y='passengers',hue ='month', data=flight)
    plt.show()
        #Also, find out how to plot the total number of passengers per year.
    sns.lineplot(x='year', y='passengers', data=flight)
    plt.show()

    #F)
    #Using dataset titanic.csv, show the counts of observations in each categorical bin using bars plot
    titanic = pd.read_csv(
        "C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW4_DataAnalysisSeaborn\\titanic.csv")

    titanicData = sns.countplot(x='Sex' ,data=titanic)
    plt.show()


main()

