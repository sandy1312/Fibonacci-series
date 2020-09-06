n=int(input("Enter ur number:"))
def fib():
    a=-1
    b=1
    if n<=0:
        print("No output")
    else:
        for i in range(n):
            c=a+b
            a,b=b,c
            print(c)
fib()