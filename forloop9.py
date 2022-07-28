#write a program to count letters in give string 
name="The easylearn academy"
find=str(input("Enter letter to search for "))
count=0
for i in name:
    if find==i:
        count+=1
print(f"letter is found {count} times")