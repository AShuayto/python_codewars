# Given number N return true if prime.
# Prime number is only divisible by 1 and itself.
# Prime numbers are greater than 1.
# Prime numbers after 2 cannot be even.

n = int(input("Enter number: "))
not1 = "Is not prime."
is1 = "Is Prime!"

def isPrime(n):
    if n == 2 or n == 1:
        print(is1)
    if n>1:
        for num in range(2,n):
            if n % num == 0:
                print(not1)
                print(str(num) + " x " + str(n//num) + " = " + str(n))
                break
        else:
            print(is1)
    else:
        print(not1)

isPrime(n)