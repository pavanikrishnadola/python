#sum,average of elements in a list without using built in function
x=[10,20,30,40,50]
s=0
c=0
for i in x:
  print(i,end=" ")
  c=c+1
  s=s+i
print()
print("count=",c)
print("sum=",s)
print("averagre=",s/c)