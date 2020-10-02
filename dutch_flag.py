A = [4,6,1,3,7]

# O(n^2) solution
def dutch_flag_partition_3(pivot_index, A):
    pivot = A[pivot_index]

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                print("part 1", A)
                break
    
    for i in reversed(range(len(A))):
        for j in reversed (range(i)):
            print(i,j)
            if A[j] > pivot:
                A[i],A[j] = A[j],A[i]
                print("part 2",A)
                break

#dutch_flag_partition(2,A)

# O(N) Time, O(1) Space
def dutch_flag_partition_2(pivot_index, A):
    pivot = A[pivot_index]
    #First psas: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
            print(A)

    #Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            #print("before", A[i], A[larger])
            A[i], A[larger] = A[larger], A[i]
           # print("after",A[i], A[larger])
            larger -= 1
            print(A)
            
def dutch_flag_partition_1(pivot_index, A):
    pivot = A[pivot_index]
    #keep the following invariants during partitioning
    #bottom group A[:smaller]
    #middle group A[smaller:equal]
    #unclassified group A[equal:larger]
    #top group A[larger:]
    smaller, equal, larger = 0, 0, len(A)

    #keep iterating as long as there is an unclassified element

    while equal < larger:
        #A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: #A[equal] > pivot
            larger -=1
            A[equal], A[larger] = A[larger], A[equal]

        print(A)

dutch_flag_partition_1(2,A)

