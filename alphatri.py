
#N=['A','B','C','D','E']
#for i in range(5):
 #   for j in range(i+1):
  #      print(N[j],end=" ")
   # print()
N=5
for i in range(N):
    ch=65
    for j in range(i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()
