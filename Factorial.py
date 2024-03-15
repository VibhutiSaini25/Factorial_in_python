#USING RECURSION

#FACTORIAL

n=int(input())
def Fact(n):
    if(n==0):
        return 1
    return n*Fact(n-1)
print(Fact(n))