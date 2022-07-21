# write a programe to find power and exponent  

base=int(input("Enter your base"))
power=int(input("Enter your power"))
count=0


answer=base*base
count+=2

while count<power:
    answer=answer*base
    count+=1
print(f"this is answer{answer}")

answer=base**power
print(f"this is answer after checking {answer}")