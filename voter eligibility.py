#voter eligibility
age=int(input("enter your age:"))
if(age>=65):
  print("Senior Citizen")
  print("Eligible to vote")
elif(age<65 and age>=18):
    print("Major Citizen")
    print("Eligibility to vote")
elif(age<18):
      print("Minor Citizen")
      print("Not Eigibile to Vote")