

my_list2 = [(7746, 6008), (1267, 6143), (4592, 9305),(4473, 2848)]


lowest_Coord = my_list2[0]  # initialize lowest element x in list
lowest_x = my_list2[0] # initialize lowest element x in list
lowest_y = my_list2[0] # initialize lowest element y in list

for tuple in my_list2:
    if tuple[0] < lowest_Coord[0]:
        lowest_x = tuple[0]
    print(tuple[1])
    if tuple[1] < lowest_Coord[1]:
        lowest_y = tuple[1]

print("X",lowest_x,"Y", lowest_y)
