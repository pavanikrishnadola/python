#program to print numbers also calculate the time taken
import time
i=1
st=time.time()
while(i<=10000000):
  print(i)
  i=i+1
et=time.time()
print("time taken=",et-st)