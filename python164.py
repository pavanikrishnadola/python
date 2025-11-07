#character pattern column
i=ord("A")
while(i<=ord("E")):
    j=ord("A")
    while(j<=ord("E")):
        print(chr(i),end=" ")
        j=j+1
    i=i+1
    print()