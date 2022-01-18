upper=0
lower=0
A = input("Enter the word to check:")
String = A.strip()
for B in String:
 if(B.isupper()):
  upper=upper+1
 elif(B.islower()):
  lower=lower+1
 elif(String.isdigit()):
  print("Enter words not numbers")
Print("Lower case:",lower)
Print("Upper case:",upper)

