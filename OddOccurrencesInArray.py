# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    my_dict=dict()
    for i in A :
        if i in my_dict.keys() :
            my_dict[i] = my_dict[i] + 1
        else :
            my_dict[i] = 1
    '''
    for x in my_dict:
        print(x)       #prints the keys
    print("All values")
    for x in my_dict.values():
        print(x)       #prints values
    print("All keys and values") '''
    for x,y in my_dict.items():
        #print(x, ":" , y)       #prints keys and values
        if y % 2 != 0:
            return x
