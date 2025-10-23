#check upper/lower/other cases
ch=input("press any key on keyboard:")
if((ch)>="A" and (ch)<="Z"):
  print("Upper case")
elif((ch)>="a" and (ch)<="z"):
  print("Lower case")
elif((ch)>='0' and (ch)<='9'):
  print("Digit")
else:
    print("Other")