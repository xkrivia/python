# CHRIS FELLI, 2019

def flattenArray(my_nest):
    # my_nest is a list, possibly nested, to ONE level
    my_flat = [] # initially empty, result list
    for my_item in my_nest:
        if type(my_item) is list:
            # if we have a list, then extend the result
            # with the item, an assumed flat list
            my_flat.extend(my_item)
        else: # otherwise append to the result, one item
            my_flat.append(my_item)
    return my_flat # now flattened list
    
def flattenArrayN(my_nest):
    # my_nest is a list, possibly nested, to ANY level
    my_flat = [] # initially empty, result list
    for my_item in my_nest:
        if type(my_item) is list:
            # if we have a list, then extend the result
            # with a recursively flattened list
            my_flat.extend(flattenArrayN(my_item))
        else: # otherwise append to the result, one item
            my_flat.append(my_item)
    return my_flat # now flattened list

print(flattenArray([1,2,3, [4,5], 6, [7,8], 9]))

print(flattenArrayN([1, 2, [3, [4, 5]], 6]))