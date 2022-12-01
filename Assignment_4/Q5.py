#program to grade marks within a range.

n=float(input("Enter the marks otained in decimal value to get grade "))
if 0<=n<0.6 :
    print("your grade is F")
elif 0.7>n>=0.6:
    print("your grade is D")
elif 0.8>n>=0.7:
    print("your grade is C")
elif 0.9>n>=0.8:
    print("your grade is B")
elif  1.0>=n>=0.9:
    print("your grade is A")
else:
    print("ERROR- verify the marks again Or enter the marks in decimal")              