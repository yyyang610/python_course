
import sys;   
import timeit



setup_list_ab = """
from __main__ import list_ab
"""
def list_ab():

  for index, a in enumerate([(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]):   
   #print(f"a[{index}] ={a}")
   y=a[0]+a[1]
   #print(y)   




def calculate_poly_range(start, end,result):
    for x in range(start, end):
        y = x**2 + 2*x + 1
        print('y = ', y)
        result.append(y)
    return result


# show call poly function with plot

def showpoly():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(-10, 10, 100)
    y = x**2 + 2*x + 1
    plt.plot(x, y)
    plt.show()

#showpoly()

#execution_time = timeit.timeit("list_ab()", setup=setup_list_ab, number=1000)
execution_time = timeit.timeit("list_ab()", setup=setup_list_ab, number=1000)
print("Execution time:", execution_time)
