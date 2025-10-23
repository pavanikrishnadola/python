#program
Sno=int(input("enter student number:"))
Sname=input("enter student name:")
Sclass=input("enter student class:")
Ssec=input("enter student section:")
M1=int(input("enter M1 marks:"))
M2=int(input("enter M2 marks:"))
M3=int(input("enter M3 marks:"))
M4=int(input("enter M4 marks:"))
M5=int(input("enter M5 marks:"))
M6=int(input("enter M6 marks:"))
tot=M1+M2+M3+M4+M5+M6
avg=tot/6
print("------------------------")
print("MARKS REPORT")
print("------------------------")
print("Sno=",Sno,"\t","Sname=",Sname)
print("Sclass=",Sclass,"\t","Ssec=",Ssec)
print("------------------------")
print("Total marks=",tot)
print("Percentage of marks=",avg)
print("------------------------")
if(M1<35 or M2<35 or M3<35 or M4<35 or M5<35 or M6<35):
  print("fail")
elif(avg>=60):
    print("Grade A")
elif(avg<60 and avg>45):
      print("Grade B")
elif(avg<45):
        print("Grade C")