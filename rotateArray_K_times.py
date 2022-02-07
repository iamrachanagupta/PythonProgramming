# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    #check for empty array
    if A == []:
        return A
    
    #check if k is equal to length of array , that case no need to rotate, just return original array
    if K == len(A) :
        return A
    
    #check if k >  length of array , then rotate only with K % len(A)
    if K > len(A) :
        K = K % len(A)
    R=[]
    R = [0 for i in range(len(A))] 
    for i in range(len(A)):
        k1 = i+K
        if(k1 > len(A) -1) :
            rot =  k1 - len(A)
        else :
            rot = k1   
        R[rot] = A[i]
        
       

    return R
