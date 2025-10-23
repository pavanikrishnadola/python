#program to count,sum and average from 1 to 5
i=1;c=0;s=0
while(i<=5):
  print(i,end=" ")
  c=c+1
  s=s+i
  i=i+1
print()
print("count=",c)
print("sum=",s)
print("average=",(s/c))