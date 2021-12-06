import copy
import numpy as np

# open the input data and save in appropriate format
with open('day_5.txt', 'r') as f:
    coordinates = f.read().split('\n')
    coordinates = [coordinate.split('->') for coordinate in coordinates]
    coordinates = [[coordinate[0].split(','), coordinate[1].split(',')] for coordinate in coordinates]
    coordinates = [[int(coordinate[0][0]),
                    int(coordinate[0][1]), 
                    int(coordinate[1][0]), 
                    int(coordinate[1][1])] for coordinate in coordinates]
    
# create helper matrix m1 the same size as original input matrix, and all zeros
m1 = np.asarray(coordinates)
m2 = np.zeros((m1.max()+1, m1.max()+1), dtype = int)


def find_points(m1):
    points = []
    for row in m1:
        if row[0] == row[2]:
            if row[1]<row[3]:
                for i in range(row[1], row[3]+1):
                    points.append([row[0],i])
            else:
                for i in range(row[3], row[1]+1):
                    points.append([row[0],i])
        if row[1] == row[3]:
            if row[0]<row[2]:
                for i in range(row[0], row[2]+1):
                    points.append([i,row[1]])
            else:
                for i in range(row[2], row[0]+1):
                    points.append([i,row[1]])
                    
    return points

def no_of_overlap_points(points, m2):
    for point in points:
        m2[point[1]][point[0]] +=1
    
    unique, counts = np.unique(m2, return_counts=True)
    score_list = dict(zip(unique, counts))
    
    score = 0
    for key in score_list:
        if key > 1:
            score += score_list[key]
            
    return score

points = find_points(m1)
score = no_of_overlap_points(points, m2)
print('No of overlap points: ', score)



