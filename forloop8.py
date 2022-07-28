#write a program to print mutlplication table of given number 
table=int(input("Enter table "))
rang=int(input("Enter value for range"))
count=1
answer=1
rang+=1
# print(f"{table} x {count} = {answer}")
for count in range(1,rang):
    answer=table*count
    print(f"{table} x {count} = {answer}")
