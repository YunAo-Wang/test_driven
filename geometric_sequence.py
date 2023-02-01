

def geom_seq(list1):
    # common factor
    r = int(list1[1] / list1[0])
    if r % 2 == 0:
        print("common factor",r)
        # geometric sequence formula
        for a in range(len(list1)):
            if list1[0]*r**a == list1[a]:
                print(list1[a])
            else:
                print("data is not a geometric sequence",list1[a])
                return list1[a]

    else:
        print("common factor is not an integer", r)
        return r


# list1 = [2, 4, 8, 16]
# geom_seq(list1)
#
# list2 = [3, 6, 12, 24]
# geom_seq(list2)
