# write a program to print following series (Lucas series)
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 300
first=2
second=1
answer=0
print(f"{first}  {second}",end=" ")
answer=first+second
print(answer,end=" ")
while answer<123:
    first=answer
    answer=answer+second
    print(answer,end=" ")
    second=answer
    answer=first+answer
    print(answer,end=" ")
print("goodebye..")