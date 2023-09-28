# User function Template for python3

def deleteFromArray(arr, n, idx):
    # code here
    # i=0
    # for i in range(idx,len(arr)-1):
    #     arr[i] = arr[i+1]

    # arr[i+1]=0
    while idx < n - 1:
        arr[idx] = arr[idx + 1]
        idx += 1

    arr[idx] = 0

if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        idx = int(input())

        arr = [i + 1 for i in range(n)]

        deleteFromArray(arr, n, idx)

        for e in arr:
            print(e, end=' ')
        print()
