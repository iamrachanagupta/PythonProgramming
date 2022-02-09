# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sum = 0
    n = len(A)
    for i in A :
        sum = sum + i
    exp_sum = (n+1) *(n + 2)//2   
    return (exp_sum - sum)
