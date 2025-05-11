'''dict1={}
list1=[123,222,321,112,114,116,118]
ave=sum(list1)/len(list1)
for i in range(len(list1)):
    for j in list1:

       if j>ave:
        dict1.setdefault(i,j)
print(dict1)'''
X,Y = input().split()

m = int(X)
n = int(Y)
a=list()
for i in range(1,m+1):
    s=input().split()
    s1 = list()
    for j in s:
        s1.append(int(j))
    a.append(s1)

for i in range(0,m):
    sum = 0
    for j in range(0,n):
        sum += int(a[i][j])
    print(sum)


