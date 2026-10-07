arr=[10,34,45,6,8,20,25,19]
min=arr[0]
max=arr[0]
for num in arr:
    if num in arr:
        if num<min:
            num=min
        if num>max:
            max=num
print("maximum no",max)
print("minimum",min)
