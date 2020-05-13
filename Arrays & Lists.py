# def shift_left(my_list):
#     g=my_list[0]
#     my_list.pop(0)
#     my_list.append(g)
#     return my_list

# def format_list(my_list):
#     s = ", "
#     list1 = []
#     list1 = my_list[0::2]
#     last_element = my_list[-1]
#     # print(list1)
#     list2 = s.join(list1)
#     list2 += " and "
#     list2 += last_element
    
#     print(list2)

# def extend_list_x(list_x, list_y):
    # for n in range(len(list_x)):
    #     # print ("The original list x is : ", list_x[n])
    #     list_x.insert(n, list_y[n])

    # list_x[0:0] = list_y
    # return list_x


# def are_lists_equal(list1, list2):
    # for n in range(len(list1)):
    #     if list1[n] not in list2:
    #         return False
    #     else:
    #         return True

    # if sum(list1) != sum(list2):
    #     return False
    # else:
    #     return True


def longest(my_list):
    sortedlist = sorted(my_list, key=len)
    print(sortedlist)
    return sortedlist[-1]



def main():
    # print("hello")
    # print(shift_left([0, 1, 2]))
    # print(shift_left(['monkey', 2.0, 1]))
    
    # my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    # format_list(my_list)

    # x = [4, 5, 6]
    # y = [1, 2, 3]
    # print(extend_list_x(x, y))
    
    # list1 = [0.6, 1, 2, 3]
    # list2 = [3, 2, 0.6, 1]
    # list3 = [9, 0, 5, 10.5]
    # print(are_lists_equal(list1, list2))
    # print(are_lists_equal(list1, list3))

    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))


if __name__ == "__main__":
    main()

   