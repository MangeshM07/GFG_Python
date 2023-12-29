def findSquareRoot(n):
    for num in range(n//2 + 1):
        if num*num == n:
            return num
        elif num * num > n:
            return num-1
        else:
            continue

def findSquareRoot_binarysearch(n):
    low = 1
    high = n
    ans = -1
    while low <= high:
        mid = (low + high)//2
        mSquare = mid * mid
        if mSquare == n:
            return mid
        elif mSquare > n:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid

    return ans


print(findSquareRoot_binarysearch(80))