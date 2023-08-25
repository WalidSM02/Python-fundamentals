import math as m


places = 12
num = 12.09876543215248333
integer_part = int(num)
fractional_part = num - integer_part
real_fractional_part = int(fractional_part*10**places)
missing_zeros = places - (int(m.log(real_fractional_part, 10))+1)

num_deci = str(integer_part)+"."+"0"*missing_zeros+str(real_fractional_part)

print(num_deci)