#Name: Alejandra Hernandez
#Date: 09-23-2020
#Prog: HW3_UsingPandas
#Desc: Demonstrate usage of Pandas

import numpy as np
import pandas as pd
import random

def main():
    print('===============================================')
    print("Question 1(a)")
    print('===============================================')
    list = [7,11,13,17]
    list_series_one = pd.Series(list)
    print(list_series_one)

    #create series w/ 5 elements all being 100.0
    print()
    list_series_two = pd.Series(100, index=[0,1,2,3,4])
    print(list_series_two)

    #series of 20 elements with random numbers
    print()
    list2 = []
    for i in range(20):
        list2.append(random.randint(0,101))
    list_series_three = pd.Series(list2)
    print(list_series_three.describe())

    #series with temperatures customice index
    print()
    header = ("Question 1(a)")
    temperature = [98.6,98.9,100.2,97.9]
    list_series_four = pd.Series(temperature,index=('Julie','Charlie','Sam','Andrea'))
    print(list_series_four)

    #make series into dict, then turn back into series
    print()
    new_dict = list_series_four.to_dict()
    print(new_dict)
    print()
    dict_to_series = pd.Series(new_dict)
    print(dict_to_series)

    print('=============================================')

    print("Question 1(b)")
    print('=============================================')

    #create data frame from a dict
    new_dict1 = {'Maxine':[99.5,87.8,90.54], 'James':[103.5,55.4,98.47],'Amanda':[75.64,54.69,98.74]}
    temperature = pd.DataFrame(new_dict1)
    print(temperature)
    print()

    #Recreate the DataFrame temperatures in Part (a) with custom indices using
    #the index keyword argument and a list
    df = pd.DataFrame(new_dict1, index=('Morning', 'Afternoon', 'Evening'))
    print(df)
    print()

    #Select from temperatures the column of temperature readings for 'Maxine'.
    print(df.loc[:,['Maxine']])
    # i. Select from temperatures the row of 'Morning' temperature readings.

    print()
    #i. Select from temperatures the row of 'Morning' temperature readings.
    print(df[:1])
    #j. Select from temperatures the rows for 'Morning' and 'Evening'temperature
    print()
    print(df.loc[['Morning','Evening'],:])

    # k. Select from temperatures the columns of temperature readings
    #for 'Amanda' and 'Maxine'.
    print()
    print(df.loc[:, ['Maxine','Amanda']])

    #l. Select from temperatures the elements for 'Amanda' and 'Maxine' in
    # the 'Morning' and 'Afternoon'.
    print()
    print(df[['Maxine', 'Amanda']].loc[['Morning','Afternoon']])

    #m. Use the describe method to produce temperatures’ descriptive statistics.
    print()
    print(df.describe())
    # n. Transpose temperatures.
    print()
    print(df.transpose())
    # o. Sort temperatures so that its column names are in alphabetical order.
    print()
    sorted_df =df.reindex(sorted(df.columns),axis=1)

    print(sorted_df)



main()