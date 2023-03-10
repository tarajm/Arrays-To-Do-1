##Shuffle

import random

# def shuffle(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         rand_index = random.randint(0, len(lst)-1)
#         # print(rand_index)
#         new_lst.append(lst[rand_index])
#         lst.pop(rand_index)
#     return new_lst

# print(shuffle([1,2,3,4,5]))

##Skyline Heights

def skyline(arr):
    highest = 0
    new_arr = []

    for i in arr:
        if i > 0:
            if i > highest:
                highest = i
                new_arr.append(i)

    return new_arr


print(skyline([-1,7,3]))
print(skyline([-1,1,1,7,3]))
print(skyline([0,4]))


#ZIP IT
#use zip function here? from codeacademy?
# lst1 = [1,2,3]
# lst2 = [4,5,6]

def zip_it(lst1, lst2):
    new_lst = []
    #conditions to make a larger list go first when it comes to a for loop
    if len(lst1) > len(lst2):
        larger_lst = lst1
    else:
        larger_lst = lst2
    
    #now create a for loop to go through the larger list and add to empty new list
    for i in range(len(larger_lst)):
        if i <= len(lst1)-1:  #if i is less than or equal to any index in list1
            new_lst.append(lst1[i])  #add i to new list
        if i <= (len(lst2)) -1:
            new_lst.append(lst2[i])
    print(new_lst)
    return new_lst

zip_it([1,2,3],[4,5,6] )


# Test for branching on Git
