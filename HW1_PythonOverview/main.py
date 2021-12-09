#Name: Alejandra Hernandez
#Date: 08-25-2020
#Desc: An overview of intro to programming
#      with python

from abc import ABC, abstractmethod
import random
import sys
import matplotlib.pyplot as plt
from tkinter import*





class Shape(ABC):
    '''The abstract shape class holds general
    information regarding shapes. Constructor sets color to red'''

    #class const
    PI = 3.14

    def __init__(self):
        '''Constructor'''
        self.__color = "RED"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
        return

    @abstractmethod
    def find_area(self):
        #abs placeholder
        pass

    @abstractmethod
    def find_volume(self):
        #abs placeholder
        pass

    def display(self):
        #format maybe
        return self.__color

class Circle(Shape):
    '''Circle'''

    def __init__(self):
        Shape.__init__(self)
        self.__radius = 1

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius
        return

    def find_area(self):
        area = Shape.PI * pow(self.__radius, 2)
        return area

    def find_volume(self):
        #abs placeholder
        pass

    def display(self):
        print("Shape: Circle")
        print("Area: ", self.find_area())

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.__side = 2.3

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side
        return

    def find_area(self):
        area = self.__side * 2
        return area

    def find_volume(self):
        #abs placeholder
        pass

    def display(self):
        print("Shape: Square")
        print("Area: ", self.find_area())


class Cube(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.__side = 5
        #all sides cube equal

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side
        return

    def find_volume(self):
        volume = self.__side * 3
        return volume

    def find_area(self):
        return "NONE"


    def display(self):
        print("Shape: Cube")
        print("Volume: ", self.find_volume())






if __name__ == '__main__':

    #creating a list
    list = []

    #var for pie chart
    numCircle = 0
    numSquare = 0
    numCube = 0

    for i in range(15):

        objNumber = random.randint(1, 3)

        if objNumber == 1:
            objNumber = Circle()
            numCircle += 1

        elif objNumber == 2:
            objNumber = Square()
            numSquare +=1

        elif objNumber == 3:
            objNumber = Cube()
            numCube +=1

        list.append(objNumber)

    #print(list[i])

    print("How Would You Like to View Your Results?")
    print("1) Console")
    print("2) File")
    print("3) Gui")
    userInput = int(input())

    if userInput == 1:
        '''prints to console'''
        for i in range(15):
            list[i].display()
            print()
            if list[i].find_area() == "NONE":
                print(list[i].find_volume())
            else:
                print(list[i].find_area())
            print("===================")

    elif userInput == 2:
        '''Asks user for file name to save as then saves output
        to file
        '''
        #saving a ref to original std
        original_stdout = sys.stdout
        fileInput = input("Enter a File Name: ")
        with open('c:\\users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW1_PythonOverview\\'
                  + str(fileInput) + '.txt' , 'w') as f:

            for i in range(15):

                f.write("\n")

                sys.stdout = f
                list[i].display()
                sys.stdout = original_stdout

                #f.write(str(list[i].display()))

                if list[i].find_area() == "NONE":

                    f.write(str(list[i].find_volume()))
                    f.write("\n")
                else:

                    f.write(str(list[i].find_area()))
                    f.write("\n")
                f.write("===================\n")

    elif userInput == 3:
        '''creates a file then loads it into tkinter window'''
        #saving a ref to original std
        original_stdout = sys.stdout
        with open('c:\\users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW1_PythonOverview\\Data.txt' , 'w') as f:

            for i in range(15):

                f.write("\n")

                sys.stdout = f
                print(list[i].display())
                sys.stdout = original_stdout

                #f.write(str(list[i].display()))

                if list[i].find_area() == "NONE":

                    f.write(str(list[i].find_volume()))
                    f.write("\n")
                else:

                    f.write(str(list[i].find_area()))
                    f.write("\n")
                f.write("===================\n")
        f.close()

        window = Tk()
        window.title('Python HW 1')
        window.geometry("500x450")

        myText = Text(window, width=50, height=20, font=("Times New Roman", 14))
        myText.pack(pady=20)

        textFile = open('c:\\users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\HW1_PythonOverview\\Data.txt','r')
        myData = textFile.read()
        myText.insert(END, myData)
        textFile.close()
        window.mainloop()

    else:
        print("Please Enter a Valid Option.")

    #for the pie chart
    pieChart = [numCircle,numSquare,numCube]
    #pieChart.append(numCircle,numSquare,numCube)
    sliceLabels = ['Circle','Square','Cube']
    plt.pie(pieChart,labels=sliceLabels)
    #title
    plt.title('Python HW 1')
    plt.show()












# See PyCharm help at https://www.jetbrains.com/help/pycharm/
