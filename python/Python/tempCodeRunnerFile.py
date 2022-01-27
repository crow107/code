 sortl3 = sorted(l3)
    second_highest = sortl3[1]

    for i in range(a):
        if second_highest == l2[i][1]:
            print(l2[i][0])