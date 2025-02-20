#user input 
physics_marks = int(input("enter marks of physics"))
math_marks = int(input("enter marks of mathematics"))
chemistry_marks = int(input("enter marks of chemistry"))
computre_marks = int(input("enter marks of computer"))
Bio_marks = int(input("enter marks of biology "))

sum_of_marks = physics_marks + math_marks + chemistry_marks + computre_marks + Bio_marks
percentage = sum_of_marks / 5

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print ("Grade C")
elif percentage >= 60:
    print ("Grade D")
elif percentage >= 40:
    print ("Grade E")
else:
    print("Grade F")
    