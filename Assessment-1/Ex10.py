dict = {}
A=input("Do you want to Add / Modify dictionary or Exit? :") 
if (A== 'Add'):
 B=input("Enter the key:")
 C=input("Enter the value:")
 dict.update({B:C})
 Print(dict)
elif(A== 'Modify'):
 D={'a':100}
 Print("Already having a:100,so enter different value to append or modify")
 E=input("Enter the key:")
 F=input("Enter the value:")
 D.update({E:F})
 Print(D)
elif (A== 'Exit'):
 Print("Exit")
