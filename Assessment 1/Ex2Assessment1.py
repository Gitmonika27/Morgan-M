a= 2000
b= 3200
for i in range(a,b+1):

   if(i%7==0 and i%5!=0):
  strings.append(str(i))
print(', '.join(strings))
