def solution(X, Y, D):
    if D : 
        count = (Y - X) // D
    else :
        return 0 
    if (Y - X) % D != 0 :
        return count + 1
    else :
        return count
