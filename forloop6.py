#write a program to use for loop on dictionary (check whether given key exist or not)
book={'name':'rich dad poor dad','pages':450,'price':1200,'weight':1.2}
user=str(input("Enter key you want to search "))
isthere=0
for key in book:
    if user==key:
        # print("key is there in dictnary")
        isthere=1   
if isthere==1:
    print("key is found")
else:
    print("key is not found")