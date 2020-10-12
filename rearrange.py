<<<<<<< HEAD
A = [4,5,7,2,1,2]

def rearrange(A):
    for i in range(len(A)):
        # sorted sorts the array segment, reverse key sorts desc or asc based on boolean (true/false)
        # in this case if i is even, reverse the order of the sort
        # print(sorted(A[i:i+2], reverse=i%2))
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)

rearrange(A)
=======
A = [1,2,3,4,5]

def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)
        #print(A[i:i+2])

rearrange(A)

>>>>>>> 3dd0f79f1c1c680ab9bae29bddabaa3cfa935b52
print(A)