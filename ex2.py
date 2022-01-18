a=int(input("Enter the starting value"))
b=int(input("Enter the Ending value"))
for i in range(a,b+1):

 if(i%7==0 and i%5!=0):
  print(i,end=",")


