#write a program to count odd and even numbers in list
numbers=[12,43,56,78,2,13,45,75,79,41,34]
even=odd=0
for i in numbers:
    # print(i)
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"even number are {even} odd number are {odd}")