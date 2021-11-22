def solution(N):
    # write your code in Python 3.6
    if N==0:
        return N
    if sum >= 9:




print(solution(16))


""""
 int lastSeen = -1;
        int secondLastSeen = -1;
        int lbs = 0;
        int tempCount = 0;
        int lastSeenNumberRepeatedCount = 0;
 
        for (int current : arr) {
            if (current == lastSeen || current == secondLastSeen) {
                tempCount ++;
            } else {
                // if the current number is not in our read list it means new series has started, tempCounter value in this case will be
                // how many times lastSeen number repeated before this new number encountered + 1 for current number.
                tempCount = lastSeenNumberRepeatedCount + 1;
            }
 
            if (current == lastSeen) {
                lastSeenNumberRepeatedCount++;
            } else {
                lastSeenNumberRepeatedCount = 1;
 
                secondLastSeen = lastSeen;
                lastSeen = current;
            }
 
            lbs = Math.max(tempCount, lbs);
        }
        return lbs;
    }
"""