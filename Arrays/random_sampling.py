import random 

k = 3
A = [2,4,5,6,7]

def random_sampling(k, A):
    for i in range(k):
        # Generate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[0:k]

B = random_sampling(k,A)
print(B)