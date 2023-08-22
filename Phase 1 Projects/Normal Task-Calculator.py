A=int(input("enter number:"))
B=int(input("enter number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
Choice=int(input("Choose a number between 1 to 4:"))
if Choice==1:
    print(A+B)
elif Choice==2:
    print(A-B)
elif Choice==3:
    print(A*B)
elif Choice==4:
    print(A/B)
else:
    print("Invalid Choice")
