# write a program to print following series (triangular numbers)
# 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... 1000
# 0  1 2 3 4 5 6
# 0  1 1 1 1 1 1
number=0
print(number,end=" ")
temp=1

while number<990 :
    number+=temp
    print(number,end=" ")
    temp+=1