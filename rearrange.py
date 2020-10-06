A = [1,2,3,4,5]

def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)
        #print(A[i:i+2])

rearrange(A)

print(A)