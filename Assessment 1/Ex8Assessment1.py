upper=0
lower=0
A = input("Enter the word to check:")
string = A.strip()
for B in string:
 if(B.isupper()):
  upper=upper+1
 elif(B.islower()):
  lower=lower+1
 elif(string.isdigit()):
  print("Enter words not numbers")
print("Lower case:",lower)
print("Upper case:",upper)