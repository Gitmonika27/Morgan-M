Import math
Num = input("Enter the values:") 
Num = Num.split(',')
Result_list=[] 
For D in Num:
 Q=round(math. Sqrt(2*50*int(D)/30))
 Result_list.append(Q)
Print(Result_list)



