# FIBONACCI SERIES

nterm = int(input("How many terms?"))
i1 = 0
i2 = 1
count = 0
fibonnaci = list()

if nterm <= 0:
    print("Enter a positive int")
elif nterm == 1:
    print("Fibonacci sequence upto", nterm, ":")
    print(i1)
else:
    print("fibonacci sequence :")
    while count < nterm:
        fibonnaci.append(i1)
        ith = i1 + i2
        i1 = i2
        i2 = ith
        count += 1

print(fibonnaci)

















