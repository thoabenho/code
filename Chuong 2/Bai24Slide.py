import math

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

S=(a+b+c)/2

Dientich=round(math.sqrt(S*(S-a)*(S-b)*(S-c)))

print("Dien tich=", Dientich, sep="")