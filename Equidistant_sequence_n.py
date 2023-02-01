def is_eq(list):
    if len(list) > 2:
        eqd = list[1] - list[0]
        for i in range(1, len(list)):
            num = list[i - 1] + eqd
            print('num', num, 'list[i]', list[i])
            if num == list[i]:
                pass
            else:
                return False, list[i:]
