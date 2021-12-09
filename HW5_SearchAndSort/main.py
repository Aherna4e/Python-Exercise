#Name: Alejandra Hernandez
#Date: 10/11/2020
#Prog: HW5_SearchAndSort

import time
import random
import numpy as np
import matplotlib.pyplot as plt

###############
#bubble sort
###############

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        for j in range(0, n - i - 1):


            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

###########
#shellsort
###########

def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            # shift earlier gap-sorted elements up until the correct
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap/ 2)

###########
#Quicksort
###########

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

#########################
#Random sort list func
#########################

def randomGeneratedList(myList,y):
    for i in range(0, y):  # create 10000 random numbers
        x = random.randint(1, 10000)  # ranges 1 to 10000
        myList.append(x)

#######################
#Display Func
#######################
def display(myList):
    for i in range(len(myList)):
        print(myList[i])

def main():


    #for bubble sort
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    randomGeneratedList(list1, 10000)
    randomGeneratedList(list2, 30000)
    randomGeneratedList(list3, 50000)
    randomGeneratedList(list4, 75000)
    randomGeneratedList(list5, 100000)


    #shell sort
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 =[]
    randomGeneratedList(list6, 10000)
    randomGeneratedList(list7, 30000)
    randomGeneratedList(list8, 50000)
    randomGeneratedList(list9, 75000)
    randomGeneratedList(list10, 100000)


    #quicksort
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    randomGeneratedList(list11, 10000)
    randomGeneratedList(list12, 30000)
    randomGeneratedList(list13, 50000)
    randomGeneratedList(list14, 75000)
    randomGeneratedList(list15, 100000)

    ####################
    # bubbbbbleee
    ####################

    ############################################################

    start_time = time.perf_counter()
    bubbleSort(list1)
    l1_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l1_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    bubbleSort(list2)
    l2_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l2_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    bubbleSort(list3)
    l3_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l3_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    bubbleSort(list4)
    l4_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l4_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    bubbleSort(list5)
    l5_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l5_Stop_time:0.2f} seconds")
    print()

    ###################################################################




####################
    #SHELL SORT
####################

    ############################################################
    start_time = time.perf_counter()
    shellSort(list6)
    l6_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l6_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    shellSort(list7)
    l7_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l7_Stop_time:0.2f} seconds")


    start_time = time.perf_counter()
    shellSort(list8)
    l8_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l8_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    shellSort(list9)
    l9_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l9_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    shellSort(list10)
    l10_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l10_Stop_time:0.2f} seconds")
    print()
###################################################################

####################
    #QUICK SORT
####################

    ############################################################
    start_time = time.perf_counter()
    quickSort(list11,0, (len(list11))-1)
    l11_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l11_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    quickSort(list12,0, (len(list12))-1)
    l12_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l12_Stop_time:0.2f} seconds")


    start_time = time.perf_counter()
    quickSort(list13, 0, (len(list13)) - 1)
    l13_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l13_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    quickSort(list14, 0, (len(list14)) - 1)
    l14_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l14_Stop_time:0.2f} seconds")

    start_time = time.perf_counter()
    quickSort(list15, 0, (len(list15)) - 1)
    l15_Stop_time = time.perf_counter() - start_time
    print(f"sort took {l15_Stop_time:0.2f} seconds")
    print()

###################################################################


    n_groups = 3

    first = (l1_Stop_time, l6_Stop_time, l11_Stop_time)
    sec = (l2_Stop_time, l7_Stop_time, l12_Stop_time)
    third = (l3_Stop_time, l8_Stop_time, l13_Stop_time)
    fourth = (l4_Stop_time, l9_Stop_time, l14_Stop_time)
    fifth = (l5_Stop_time, l10_Stop_time, l15_Stop_time)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.10
    opacity = 0.90

    rects1 = plt.bar(index, first, bar_width,
                     alpha=opacity,

                     label='10000')

    rects2 = plt.bar(index + bar_width, sec, bar_width,
                     alpha=opacity,

                     label='30000')
    rects3 = plt.bar(index + bar_width * 2, third, bar_width,
                     alpha=opacity,

                     label='50000')
    rects4 = plt.bar(index + bar_width * 3, fourth, bar_width,
                     alpha=opacity,

                     label='75000')
    rects5 = plt.bar(index + bar_width * 4, fifth, bar_width,
                     alpha=opacity,

                     label='100000')

    plt.xlabel('Algorithms')
    plt.ylabel('Time (Seconds)')
    plt.title('Times of Sorting Algorithms')
    plt.xticks(index + bar_width, ('Bubble Sort', 'Shell Sort', 'Quick Sort'))
    plt.legend()

    plt.tight_layout()
    plt.show()

main()




''' 
from the visualization chart, it is clear
that the bubble sort algorithm is extremely inefficient
'''

