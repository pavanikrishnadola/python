#finding exact count of charcters in string
c=0
x="state bank of india"
for i in x:
  if(i==""):
    continue
  c=c+1
print("number of charcters=",c)