A = [1,2,3,4,5,6]

# O(N) Time | O(N) Space
def evens_odds1(A):
    i = 0
    temp = []
    while i != len(A):
        if A[i] % 2 == 0: 
            temp.append(A[i])
            A.remove(A[i]) 
            i -=1
        i += 1
    return temp + A 

# print(evens_odds1(A))

# Sort in place - takes O(N/2) Time | O(1) Space
# Sorting in place with O(N) would repeat some cycles
# Which can lead to reshuffling the odds again (unneeded work)
def evens_odds2(A):
    i = 0
    j = len(A)-1
    middle = j // 2

    while i <= middle:
        if A[i] % 2 != 0:
            A.append(A[i])
            A.remove(A[i])        
        i += 1

    assert A == [2,4,6,1,3,5]
    return A

# print(evens_odds2(A))

# EPI Solution O(N/2) Time | O(1) Space
def evens_odds3(A):
    i = 0
    j = len(A) - 1

    while i < j:
        if A[i] % 2 == 0:
            i += 1
        else:
            # A[i] is odd
            # swap in one line
            A[i], A[j] = A[j], A[i]
            j -= 1
    return A

print(evens_odds3(A))