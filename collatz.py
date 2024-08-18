#Collatz conjecture
def collatz_conjecture(n):
    while n!=1:
        if n % 2 ==0:
            n = n/2
        else:
            n = 3*n +1
        print("{}---->".format(n),end="")
Number = int(input("Enter a number: "))
collatz_conjecture(Number)
