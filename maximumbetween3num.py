#input numbers

Num1 = int(input("num 1"))
Num2 = int(input("num 2"))
Num3 = int(input("num 3"))

# find maximum number 
if Num1 > Num2 and Num1 > Num3:
    print("maximum num 1")
elif Num2 > Num3:
    print("maximum num 2")
else:
    print("maximum num 3")
