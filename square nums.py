# SQUARE NUMBER SERIES

nterm = int(input("How many terms?"))
count = 0
i = count + 1
squarelist = list()
if nterm <= 0:
    print("Enter a positive int")
elif nterm == 1:
    print("Square sequence upto", nterm, ":")
    print(i)
else:
    while count < nterm:
        i = count + 1
        sqr = i * i
        squarelist.append(sqr)
        count += 1
    print(squarelist)
