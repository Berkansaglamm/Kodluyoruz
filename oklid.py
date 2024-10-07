def euclideanDistance(points_1, points_2):
    return ((points_2[0] - points_1[0])**2 + (points_2[1] - points_1[1])**2)**0.5


points = [(1,2), (3,4), (5,6), (7,8), (9,10)]

distances = [euclideanDistance(points[i], points[i+1]) for i in range(len(points)-1)]

print(distances)