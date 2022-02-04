import math

Num = input("Enter the values:") 
Num = Num.split(',')
Result_list=[] 
for D in Num:
    Q = round(math.sqrt(2*50*int(D)/30))
    Result_list.append(Q)
print(Result_list)