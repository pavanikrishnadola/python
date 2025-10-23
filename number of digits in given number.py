#count the number of digits in given number
c=0
n=int(input("Enter the number:"))
if n == 0:
    c = 1
else:
    n = abs(n)
    while(n > 0):
      n = n//10
      c=c+1
print("count=",c)