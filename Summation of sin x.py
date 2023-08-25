# term       : term is the first number of the series combination.
# total      : is the sum of the series.
# factor     : is the difference of the denominator
# count      : Number of steps done to calculate the sum of an infinite series.
# Tollerence : Tollerence is the approximate least value of a term which is probably the last digit of a series.


import simple_colors as sp
from time import process_time, ctime
t1_start = process_time()
import math as m

Tollerence = 1.0e-17
x = float(input("Enter a value in degrees :  "))
term = m.radians(x)
xsquard = term**2
factor = 2
total = 0
count = 1

while abs(term)> Tollerence:
    total+=term
    term = -1*term*xsquard/(factor*(factor+1))
    factor+=2
    count+=1
    
print(sp.yellow("""
      
      the Python value for sin(%d)is :  %f
      the approximate value for sin(%d) is : %.15f
      Number of steps : %d
      """ %(x, m.sin(m.radians(x)), x, total, count),('bright', 'bold')))
print("""
      Programmed by:
          SM Walid
          Data scientist at Datacamp.
          Date:%s
      """%ctime())


t1_stop = process_time()
print(f"\nFinished in {t1_stop-t1_start} seconds")