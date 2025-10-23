#(2)check upper/lower/other cases
ch=input("press any key on keyboard:")
if(ord(ch)>=65 and ord(ch)<=90):
  print("Upper case")
elif(ord(ch)>=97 and ord(ch)<=122):
  print("Lower case")
elif(ord(ch)>=48 and ord(ch)<=57):
  print("Digit")
else:
    print("Other")