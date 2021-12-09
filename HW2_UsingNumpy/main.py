#Name: Alejandra Hernandez
#Date: 09/12/2020
#Program:HW2_UsingNumpy
#Desc: 1). Demonstrate knowledge in usage of basic numpy procedures
#      2). Manipulate data from .csv files


import numpy as np
from numpy import genfromtxt
import csv
from scipy import stats
import matplotlib.pyplot as plt

import statistics as st

def main():
    print("==========================================================================")
    print("QUESTION 1")
    print("==========================================================================")
    myList = np.arange(1, 16)
    print(myList)
    print()

    newList = myList.reshape(3,5)
    print(newList)
    print()

    #select second row
    print(newList[1])
    print()

    #select column 4
    print(newList[:,4])
    print()

    #select rows 0,1
    print(newList[0:2])
    print()

    #select columns 2-4
    print(newList[:,2:4])
    print()

    #row 1 col 4
    print(newList[0:1,4])
    print()

    #row 1,2 columns 0,2,4
    print(newList[1:3,0::2])
    print("==========================================================================")
    print("QUESTION 2")

   # with open('C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW2_UsingNumpy\\Student_Grades.csv', 'r') as f:
      #  gradesData = list(csv.reader(f))

    #grades = np.array(gradesData[1:], dtype =np.float)

    print("==========================================================================")
    gradesData = np.genfromtxt('C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW2_UsingNumpy\\'
                               'Student_Grades.csv', delimiter=',', skip_header=1)
    print(gradesData)
   # print()
    print("==========================================================================")
    numStudents = gradesData.shape[0]
    print("Number of Students:",numStudents)
    print("Rows and Columns:" ,gradesData.shape)
    print("Data Type:", gradesData.dtype)
    print("==========================================================================")
    stuData = gradesData[:,-1]
    print("Student Data:",stuData)
    print("==========================================================================")
    print("Min score: ", stuData.min())
    print("Max score: ", stuData.max())
    print("Average score: ", stuData.mean())
    print("Mode Score: ", stats.mode(stuData))
    print("Median score:", st.median(stuData))
    print("Std. Dev.:", stuData.std())

    print("25th Percentile: ", np.percentile(stuData,25))
    print("75th Percentile: ", np.percentile(stuData, 75))
    print("==========================================================================")

    #Slice a values
    A_Data = stuData >= 90
    A_Num = stuData[A_Data].shape[0]
    print("Number of A's:", A_Num)

    # Slice b values
    B_Data = (stuData <90) & (stuData >= 80)
    B_Num = stuData[B_Data].shape[0]
    print("Number of B's:",B_Num)

    # Slice c values
    C_Data = (stuData <80) & (stuData >= 70)
    C_Num = stuData[C_Data].shape[0]
    print("Number of C's:",C_Num)

    # Slice d values
    D_Data = (stuData <70) & (stuData >= 60)
    D_Num = stuData[D_Data].shape[0]
    print("Number of D's:",D_Num)

    # Slice F values
    F_Data = (stuData <60)
    F_Num = stuData[F_Data].shape[0]
    print("Number of F's:",F_Num)
    print("==========================================================================")
    gradesPieChart = [A_Num,B_Num,C_Num,D_Num,F_Num]
    sliceLabels = ['A', 'B', 'C','D','F']
    plt.pie(gradesPieChart, labels=sliceLabels)
    # title
    plt.title('Student\'s Grades')
    plt.show()


main()