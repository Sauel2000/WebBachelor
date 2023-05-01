import math

# Define a function to calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

# Define the distance threshold for grouping points
dist_threshold = 20

# Define the initial list of points
points = [(1,2), (3,4), (5,6), (10,12), (15,16), (17,19), (22,24), (24,28), (30,32)]

# Create an empty list to store the groups of points
groups = []

# Loop through all points and check if they are close to any other points
for i in range(len(points)):
    # Create a new group with the current point
    current_group = [points[i]]
    
    # Check if any other points are close to the current point
    for j in range(i+1, len(points)):
        if distance(points[i], points[j]) <= dist_threshold:
            current_group.append(points[j])
    
    # Check if the current group overlaps with any existing groups
    group_overlap = False
    for group in groups:
        if any([point in group for point in current_group]):
            group.extend(current_group)
            group_overlap = True
            break
    
    # If the current group does not overlap with any existing groups, add it to the list of groups
    if not group_overlap:
        groups.append(current_group)

# Loop through all the groups and look for the furthest point within each group
for group in groups:
    # Find the point that is furthest away from the first point in the group
    furthest_point = group[0]
    furthest_distance = 0
    for point in group:
        if distance(group[0], point) > furthest_distance:
            furthest_point = point
            furthest_distance = distance(group[0], point)
    
    # Create a new group with the furthest point
    new_group = [furthest_point]
    
    # Loop through all other points in the same group and check if they are within 20 pixels
    for point in group:
        if point == furthest_point:
            continue
        if distance(furthest_point, point) <= dist_threshold:
            new_group.append(point)
    
    # Add the new group to the list of groups
    groups.append(new_group)

    # Remove the original group from the list of groups
    groups.remove(group)

# Print out the final list of groups
print(groups)
