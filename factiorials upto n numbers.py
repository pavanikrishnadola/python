#factiorials upto n numbers
i=1;f=1
n=int(input("enter the number:"))
print("Number\tFactoreial")
print("-----------------------")
while(i<=n):
  f=f*i
  print(i,"\t",f)
  i=i+1