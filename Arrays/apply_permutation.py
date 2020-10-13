A = [6,7,8,9]
perm = [3,0,1,2]

# O(N) Time, O(1) Space
def apply_permutation(perm, A):
    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative.
        next = i 
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
           
            # Subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp 
    # Restore perm
    perm[:] = [a + len(perm) for a in perm]


# apply_permutation(perm, A)
# print(A)

# O(n^2) Time
def apply_permutation2(perm, A):
    def cyclic_permutation(start, perm, A):
        i, temp = start, A[start]
        while True:
            next_i = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i, next_temp
            if i == start:
                break
 
    for i in range(len(A)):
        # Traverses the cycle to see if i is the minimum element
        j = perm[i]
        while j != i:
            if j < i:
                break
            j = perm[j]
        else:
            cyclic_permutation(i, perm, A)

# apply_permutation2(perm, A)
# print(A)