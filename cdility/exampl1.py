
def solution(A):
    # write your code in Python 3.6
    count = 0
    j=0
    for i in range(0,len(A)):
        j=i+1
        for j in range(0,len(A)):
            if A[i] == A[j]:
                count += 1
    return count


A =  [3, 5, 6, 3, 3, 5]
print(solution(A))