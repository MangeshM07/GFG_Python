def sum1(n):
    result=0
    for i in range(1,n+1):
        result += i

    print(result)

def sum2(n):
    result = (n * (n+1))/2
    print("Sum2 result "+str(result))

sum1(1000000)
sum2(1000000)