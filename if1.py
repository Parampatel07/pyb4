# write a programe to find largest triangle among the given three triangle 
height1=int(input("Enter height for 1 triangle  "))
base1=int(input("Enter base for 1 triangle  "))

area1=height1*base1/2

height2=int(input("Enter height for 2 triangle  "))
base2=int(input("Enter base for 2 triangle  "))

area2=height2*base2/2


height3=int(input("Enter height for 3 triangle  "))
base3=int(input("Enter base for 3 triangle  "))

area3=height3*base3/2

print(area1," this is area 1")
print(area2," this is area 2")
print(area3," this is area 3")

if area1==area2 and area2==area3:
    print("all are same")
else:
    if area1>area2:
        if area1>area3:
            print("area 1 is greater than all")
        else:
            print("area 3 is greater than all")
    else:
        if area2>area3:
            print("area 2 is greater than all")
        else:
            print("area 3 is greater than all")