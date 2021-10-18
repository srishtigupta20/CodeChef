# cook your dish here
T = int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    if(A==7 or B==7 or C==7 ):
        print("Yes")
    else:
        print("No")

