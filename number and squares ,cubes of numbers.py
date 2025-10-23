#print number and squares ,cubes of numbers
i=1
n=int(input("Enter the number:"))
print("Number\tSquares\tCubes")
print("-------------------------")
while(i<=n):
  print(i,"\t",i*i,"\t",i*i*i)
  i=i+1