import math

distance = 0

def calculate_distance(point1,point2):
    return math.sqrt( ((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2) )

def get_points_distance(centroids,pts):
    distance = 0
   
    print("\nDistance table :")
    print(" Data points |", end =" "),
    cent_len = 15
    for center in centroids :
        print(str(center)+" |",end =" "),
        cent_len = cent_len + len(str(center)) + 3
    print("\n",end=""),
    print("-"*(cent_len - 1))  
    for point in pts :
        print("  ",point," "*(7-len(str(point)))," |",end =" ")
        for center in centroids :
            distance = round(calculate_distance(center,point),2)
            print(distance,end =""),
            print(" "*(1+len(str(center))-len(str(distance))),end ="")
            print("|",end =" ")
        print("\n")

def get_inter_distance(points):
    a=[]
    for p1 in points:
        b=[]
        for p2 in points:
            b.append(round(calculate_distance(p1,p2),2))
        a.append(b)
    return a


centroids = [
    [1.33,3.33],[4.5,1.5],[7.67,5.67]
    #(1,2), (11,4) , (5,17), (6,3), (8,5),(9,9), (2,4), (4,2)
    ]
pts  = [
    (1,2), (1,4) , (5,1), (6,3), (8,5),(9,9), (2,4), (4,2)
]
get_points_distance(centroids,pts)
data = get_inter_distance(pts)
