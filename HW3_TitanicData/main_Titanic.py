#Name: Alejandra Hernandez
#Date: 09-23-2020
#Prog: HW3_UsingPandas
#Desc: Demonstrate usage of Pandas gather data titanic.csv
import csv
import pandas as pd


def main():
    data = pd.read_csv('C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW3_TitanicData\\titanic.csv')

    #a) How many passengers were in the titanic?
    num_passengers = data.shape[0]
    print('Number of Passengers: ', num_passengers)
    print()

    #b) How many male and female passengers were in the titanic?
    print(data.groupby("sex")['passengerClass'].count())
    '''female_df = data[data['sex'] == 'female'].count()
    male_df = data[data['sex'] == 'male'].count()
    print(female_df)
    print(male_df)'''
    #c) What was the average age of all passengers?
    print()
    print("Average age: ", data['age'].mean())

    #d) How many passengers under 21 years of age?
    print()
    under_21 = data[data['age'] < 21].shape[0]
    print("Number of Passengers Under 21: ", under_21)

    #e) How many survived and how many did not? How many males and how many females?
    print()
    #print(data.groupby(['sex']).size())
    print(data.groupby(['survived', 'sex']).size())

    # g) Display the name of all passengers that survived.
    print()
    new_data = (data[(data.survived == 'yes')])
    print(new_data['Name'])

    #f) What was the youngest age that survived, and the oldest age? What were their names.
    print()
    #min_age = new_data['age'].min()
    #print("Youngest Survivor: ",min_age)
    #max_age = new_data['age'].max()
    #print("Oldest survivor: ",max_age)
    print(new_data[new_data.age == new_data.age.min()])
    print()
    print(new_data[new_data.age == new_data.age.max()])





main()