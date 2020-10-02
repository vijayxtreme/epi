A = [1,3,3,7,11,4,4,1,2]

def delete_duplicates(A):
    A.sort()
    print(A)
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index -1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    
    return write_index

delete_duplicates(A)