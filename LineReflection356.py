def LineReflection356(points):
    if len(points) < 2:
        return False
    middle = max(points)[0] + min(points)[0] # abscissa
    set_of_points = set([(i, j) for i, j in points])
    for i, j in points:
        if (middle - i, j) not in set_of_points:
            return False
    return True
  
points1 = [[5,1],[3,1],[1, 1],[2,5],[4, 5],[4, 5]]
points2 = [[5,1],[4, 5]]
points3 = [[-1, 1], [1, 1]]
points4 = [[0, 0]]

LineReflection356(points1)
