#Input Three sides of triangle

side_a = int(input("enter side a"))
side_b = int(input("enter side b"))
side_c = int(input("enter side c"))

#check triangle valid or not
if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c >side_a:
    print("Triangle Valid")
else:
    print("Triangle not valid")
