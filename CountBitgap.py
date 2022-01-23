N = 74901729
binary = bin(N)[2:]
print (binary)
max_len = 0
new_max = 0
bit = 0
flag = False
for i in binary :
    if i == '1' and flag:
        if(max_len > new_max) :
            new_max = max_len
            #print (max_len)
        max_len = 0
        
    if i == '1' and flag == False :
        flag = True    
    if i == '0' and flag == True:
        max_len = max_len + 1
            
print (new_max)
            