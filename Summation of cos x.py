from time import process_time
t1_start = process_time()
import math as m

Tollerence = 1.0e-17
x = float(input("Enter the angle in degrees : "))
degree = m.radians(x)
term = 1
xsquard = degree**2
total = 0
count =1
factor = 1
while abs(term)> Tollerence:
    total+=term
    term = -1*term* xsquard/(factor*(factor+1))
    count+=1
    factor+=2
    
print("""
      
      The python value for cos(%d) is :  %f
      The approximate value for cos(%d): %f
      The number steps is done : %d""" %(x, m.cos(degree), x, total, count))
t1_stop = process_time()
print(f"\nFinished in {t1_stop-t1_start} seconds")
