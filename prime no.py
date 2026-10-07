num= int(input("enter the any num "))
flag=0
for i in range (2,(num//2)+1):
    flag=1
    break
if(flag==1):
    print("not prime")
else:
    print("prime")