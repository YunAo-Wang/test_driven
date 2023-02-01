def is_eq_seq(list):
    list.sort()
    for i in range(len(list) - 2):
        if list[i + 1] - list[i] != list[i + 2] - list[i + 1]:
            return False
    return True


def eq_seq(eq1, eq2):
    if is_eq_seq(eq1):
        if is_eq_seq(eq2):
            if len(eq1) == len(eq2):  # same number of items
                eqd1 = eq1[1] - eq1[0]
                eqd2 = eq2[1] - eq2[0]
                if eqd1 == eqd2:  # same difference d
                    list = []
                    for i in range(len(eq1)):
                        eq = eq1[i] + eq2[i]
                        list.append(eq)
                    return is_eq_seq(list)
            else:
                return False
        return True
    else:
        print("sequence is not an arithmetic sequence")
        return False


