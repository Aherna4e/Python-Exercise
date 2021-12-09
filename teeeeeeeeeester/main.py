import time
import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    n_groups = 3

    first = (1,2,3)
    sec = (4,5,6)
    third = (7,8,9)
    fourth = (10,11,12)
    fifth = (13,14,15)

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
    rects3 = plt.bar(index + bar_width*2, third, bar_width,
                     alpha=opacity,

                     label='50000')
    rects4 = plt.bar(index + bar_width*3, fourth, bar_width,
                     alpha=opacity,

                     label='75000')
    rects5 = plt.bar(index + bar_width*4, fifth, bar_width,
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