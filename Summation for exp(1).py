from time import process_time
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


def decimal_places(num, places):
    integer_part = int(num)
    fractional_part = num - integer_part
    real_fractional_part = int(fractional_part*10**places)
    missing_zeros = places - (int(m.log(real_fractional_part, 10))+1)

    num_deci = str(integer_part)+"."+"0"*missing_zeros+str(real_fractional_part)
    return num_deci


places = int(input("How many decimal places you want : "))
approxi_val =decimal_places(total, places)
real_val = decimal_places(m.exp(1), places)
    
print("""
       The python value for exp(1) is : %s
       The approximate value for exp(1) is : %s
       Number of steps : %d""" %(real_val, approxi_val, count))

t1_stop = process_time()
print(f"\nFinished in {t1_stop-t1_start} seconds")
# print("\nFinished in ",(t1_stop-t1_start), "seconds")

       
