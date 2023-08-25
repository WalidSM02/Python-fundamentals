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
term = 1
count = 1
total = 0
factor = 0
while abs(term)>Tollerence:
    total+=term
    term = term/(factor+1)
    factor+=1
    count+=1

"""Created a function called decimal_places() to identify the required decmal place number."""
def decimal_places(num, places):
    integer_part = int(num)
    fractional_part = num - integer_part
    real_fractional_part = int(fractional_part*10**places)
    missing_zeros = places - (int(m.log(real_fractional_part, 10))+1)

    num_deci = str(integer_part)+"."+"0"*missing_zeros+str(real_fractional_part)
    return num_deci


places = int(input("How many decimal places you want : "))

# Real value of exp(1), which is the sum of infinite series of exp(1) 
approxi_val =decimal_places(total, places)

# Python value of the exp(1)
real_val = decimal_places(m.exp(1), places)
    
print(sp.yellow("""
       The python value for exp(1) is : %s
       The approximate value for exp(1) is : %s
       Number of steps : %d""" %(real_val, approxi_val, count), 'bright'))
       
print("""
      Programmed by:
          SM Walid
          Data scientist at Datacamp.
          Date:%s
      """%ctime())

t1_stop = process_time()
print(f"\nFinished in {t1_stop-t1_start} seconds")


       
