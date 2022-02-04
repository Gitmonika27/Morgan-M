n = int(input("Enter value for factorial:"))
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
Print("Answer is", factorial(n))

