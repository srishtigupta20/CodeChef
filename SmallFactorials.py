#Python program
for a in range(int(input())):
    n=int(input())
    factorial=1
    if n>1:
        for i in range(1,n+1):
            factorial = factorial*i
    print(factorial)
