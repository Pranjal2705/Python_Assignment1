#create one empty list add prime no to list 50

primenum_list=[]
for num in range(1,51):
    if num>1:
        for i in range(2,num):
            if(num%2==0):
                break
        else:
            primenum_list.append(num)
print(primenum_list)
