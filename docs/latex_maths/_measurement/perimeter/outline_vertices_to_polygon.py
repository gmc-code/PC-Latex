'''
Explanation:
neighbors Function:
Generates neighboring coordinates for a given coordinate.
get_angle Function:
Calculates the angle between two direction vectors.
fill_polygon Function:
Takes an outline of a polygon and fills in the interior points.
Iterates over each edge of the outline and adds the points along the edge to a set.
Fills the interior of the polygon by toggling an “inside” flag as it encounters points on the edges.
Example Usage:
The outline is given as [(3, 0), (4, 0), (4, 3), (0, 3), (0, 2), (3, 2)].
The fill_polygon function generates the filled polygon points and prints them.
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

def fill_polygon(outline):
    # Initialize a set to store the filled polygon points
    filled_polygon = set()

    # Iterate over each edge of the outline
    for i in range(len(outline)):
        pt1 = outline[i]
        pt2 = outline[(i + 1) % len(outline)]

        # Determine the direction of the edge
        if pt1[0] == pt2[0]:  # Vertical edge
            x = pt1[0]
            y_start, y_end = sorted([pt1[1], pt2[1]])
            for y in range(y_start, y_end + 1):
                filled_polygon.add((x, y))
        elif pt1[1] == pt2[1]:  # Horizontal edge
            y = pt1[1]
            x_start, x_end = sorted([pt1[0], pt2[0]])
            for x in range(x_start, x_end + 1):
                filled_polygon.add((x, y))
        else:  # Diagonal edge (should not happen in a grid-based polygon)
            raise ValueError("Outline contains diagonal edges, which are not supported.")

    # Fill the interior of the polygon
    min_x = min(pt[0] for pt in outline)
    max_x = max(pt[0] for pt in outline)
    min_y = min(pt[1] for pt in outline)
    max_y = max(pt[1] for pt in outline)

    for x in range(min_x, max_x + 1):
        inside = False
        for y in range(min_y, max_y + 1):
            if (x, y) in filled_polygon:
                inside = not inside
            if inside:
                filled_polygon.add((x, y))

    return list(filled_polygon)

# Example usage
outline = [(3, 0), (4, 0), (4, 3), (0, 3), (0, 2), (3, 2)]
filled_polygon = fill_polygon(outline)
print(filled_polygon)
# this is not sorted with points adjacent
# [(1, 3), (4, 0), (1, 2), (4, 3), (3, 1), (0, 3), (4, 2), (3, 0), (2, 3), (0, 2), (3, 3), (2, 2), (3, 2), (4, 1)]