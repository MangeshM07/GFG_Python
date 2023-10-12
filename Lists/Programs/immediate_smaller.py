# User function Template for python3

class Solution:
    def immediateSmaller(self, arr, n, x):
        # return required ans

        # code here
        arr1 = sorted(arr)

        for i in range(len(arr1)):
            if arr1[i] >= x and i == 0:
                return -1
            elif arr1[i] > x:
                return arr1[i - 1]
            i += 1

        if arr1[i] < x:
            return arr1[i]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(e) for e in input().split()]
        x = int(input())
        ob = Solution()
        ans = ob.immediateSmaller(arr, n, x)
        print(ans)
# } Driver Code Ends