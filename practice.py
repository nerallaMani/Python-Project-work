import time
n=int(input("enter any number: "))
st=time.time()
for i in range(1,n+1):
    if i==400:break
    print("MG Hector")
et=time.time()
print('total time taken is: ',et-st)