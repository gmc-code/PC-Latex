'''This code effectively traces the outer boundary of the given set of polygon tiles.
'''
import math

def neighbors(coord):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in directions:
        yield (coord[0] + dir[0], coord[1] + dir[1])


def get_angle(dir1, dir2):
    angle = math.acos(dir1[0] * dir2[0] + dir1[1] * dir2[1])
    cross = dir1[1] * dir2[0] - dir1[0] * dir2[1]
    if cross > 0:
        angle = -angle
    return angle

def trace(p):
    # If the list of points is empty or has only one point, return it as is
    if len(p) <= 1:
        return p

    # Start at the lowest point, futhest to the left
    pt0 = min(p, key=lambda t: (t[1], t[0]))

    '''
    The min function is used to find the minimum value in the list p.
    The key parameter specifies a function to be called on each element before making comparisons.
    key=lambda t: (t[1], t[0]):
    This is a lambda function that takes a point t (which is a tuple (x, y)) and returns a tuple (t[1], t[0]).
    Essentially, it swaps the coordinates, so the comparison is based on the y value first and then the x value.
    How It Works
    Sorting by y Coordinate:
    The min function will first compare the y coordinates of all points.
    This ensures that the point with the smallest y value is considered first.
    Sorting by x Coordinate:
    If there are multiple points with the same y value, the x coordinate is used as a tiebreaker.
    This ensures that among points with the same y value, the point with the smallest x value is chosen.
    '''
    # Initial direction is upwards; in computer graphics, the y-coordinate increases as you move downwards and decreases as you move upwards.
    dir = (0, -1)
    pt = pt0
    # Initialize the outline with the starting point
    outline = [pt0]

    while True:
        pt_next = None
        angle_next = 10  # Dummy value to be replaced with the smallest angle
        dir_next = None

        # Find the leftmost neighbor
        for n in neighbors(pt):
            if n in p:
                # Calculate the direction vector to the neighbor
                dir2 = (n[0] - pt[0], n[1] - pt[1])
                # Calculate the angle between the current direction and the neighbor direction
                angle = get_angle(dir, dir2)
                # Update the next point if this angle is smaller
                if angle < angle_next:
                    pt_next = n
                    angle_next = angle
                    dir_next = dir2

        if angle_next != 0:
            # Add the next point to the outline
            outline.append(pt_next)
        else:
            # If the angle is zero, replace the last point in the outline
            outline[-1] = pt_next

        # If the next point is the starting point, the outline is complete
        if pt_next == pt0:
            return outline[:-1]

        # Move to the next point and update the direction
        pt = pt_next
        dir = dir_next

new_tile = [(1, 3), (4, 0), (1, 2), (4, 3), (3, 1), (0, 3), (4, 2), (3, 0), (2, 3), (0, 2), (3, 3), (2, 2), (3, 2), (4, 1)]
polygon_tiles = [(3, 0), (4, 0), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]
outline = trace(new_tile)
print(outline)
#  [(3, 0), (4, 0), (4, 3), (0, 3), (0, 2), (3, 2)]