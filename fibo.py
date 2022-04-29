
# nth_fib(4) == 2
# Because 2 is the 4th number in the Fibonacci Sequence.
# For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
# 0,1,1,2,3,5,8,13,21,34

def nth_fib(n):
    first0 = 0
    second0 = 1
    a = 0
    b = 1
    c = 0

    if n == 1:
        return(0)
    elif n == 2:
        return(1)
    else:
        for num in range(2,n):
            c = a + b
            a = b
            b = c
        return(c)

print(nth_fib(int(input("Enter Number: "))))