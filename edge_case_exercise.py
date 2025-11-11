def move(my_list, direction):

    
    index_of_1 = my_list.index(1)
    list_length=len(my_list)

    
    if direction == 'right':
        if index_of_1<list_length-1:
            my_list[index_of_1] = 0
            my_list[index_of_1 + 1] = 1

    elif direction == 'left':
        if index_of_1>0:
            
            my_list[index_of_1] = 0
            my_list[index_of_1 - 1] = 1

    return my_list
