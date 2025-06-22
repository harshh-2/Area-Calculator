import math
F=math.pi
E=0
A=(input("Enter shape:")).lower()
if(A=="square"):
    B=float(input("Enter side:"))
    E=B*B
elif(A=="rectangle"):
   B=float(input("Enter length:"))
   C=float(input("Enter breadth:"))
   E=B*C
elif(A=="circle"):
    B=float(input("enter radius:"))
    E=F*B*B
elif(A=="cube"):
    B=float(input("Enter side:"))
    E=6*B*B
elif(A=="cuboid"):
    B=float(input("Enter length:"))
    C=float(input("Enter breadth:"))
    D=float(input("Enter height:"))
    E=2*(B*C+C*D+D*B)
elif(A=="triangle"):
    B=float(input("Enter base:"))
    C=float(input("Enter height"))
    E=B*C*(1/2)
elif(A=="sphere"):
        B=float(input("Enter radius:"))
        E= 4*F*B*B
elif(A=="trapezium"):
    B=float(input("Enter parallel side1 :"))
    C=float(input("Enter parallel side2:"))
    D=float(input("Enter height:"))
    E=(1/2)*(B+C)*D
elif(A=="parallelogram"):
   B=float(input("Enter length:"))
   C=float(input("Enter breadth:"))
   E=B*C
elif(A=="hemisphere"):
        B=float(input("Enter radius:"))
        E= 3*F*B*B
elif(A=="cone"):
        B=float(input("Enter radius:"))
        C=float(input("Enter slant height"))
        E= F*B*(B+C)
elif(A=="cylinder"):
        B=float(input("Enter radius:"))
        C=float(input("Enter height"))
        E= 2*F*B*(B+C)
else:
     print("Invalid shape or check spelling ")
     exit()
print(f"AREA IS: {E}")