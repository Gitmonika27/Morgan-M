def checkKey(d,key):
    if key in d:
        print("present")
        print("values=",d[key])
    else:
        print("Not present")

d={}
user_input=int(input("enter the dictionary count:"))
for i in range(0,user_input):
    key=input("Enter the key:")
    value=input("Enter the value:")
    d[key]=value
print("dict values:",d)
key = input("enter the key:")
checkKey(d,key)