obj = [2, 3, 5, 7, 9]
n=len(obj)

for i in obj:
    print(i)
#print("\n")
print("****************************")
for i in range(2,n):
    print(obj[i])
#print("\n")
print("****************************")
# range(i,j) -> iterate from i to j-1
sum = 0
for i in range(1,6):
    sum=sum+i
    print(i)
print("Sum = {}".format(sum))
print("****************************")
# range(n) -> iterate from 0 index to n-1
for i in range(n):
    print("{} : {}".format(i, obj[i]))
print("****************************")
for i in range(1,10,2):
    print(i)
print("****************************")
for i in range(1,10,5):
    print(i)