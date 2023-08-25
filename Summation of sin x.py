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
    
print("""
      
      the Python value for sin(%d)is :  %f
      the approximate value for sin(%d) is : %.15f
      Number of steps : %d
      """ %(x, m.sin(m.radians(x)), x, total, count))