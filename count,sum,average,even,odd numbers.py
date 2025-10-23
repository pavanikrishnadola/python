#program to print count,sum,average,even,odd numbers between 1 and 5
i=1;c=0;s=0;se=0;ce=0;so=0;co=0
while(i<=5):
  print(i,end=" ")
  c=c+1
  s=s+i
  if(i%2==0):
    ce=ce+1
    se=se+i
  else:
    co=co+1
    so=so+i
  i=i+1
print()
print("count of all=",c)
print("sum of all=",s)
print("average of all=",(s/c))
print("-------------------------")
print("count of even=",ce)
print("sum of even=",se)
print("average of even=",(se/ce))
print("-------------------------")
print("count of odd=",co)
print("sum of odd=",so)
print("average of odd=",(so/co))
print("-------------------------")