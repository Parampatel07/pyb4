#write a program to count negative value in tuples 
number=(12,-45,10,23,-65,-78,-45,54,65,32)
count=0
for value in number:
    if value<0:
        count+=1
print(count)