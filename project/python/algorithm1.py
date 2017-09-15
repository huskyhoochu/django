def selection_sort(list):
    for j in range(len(list)):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            else:
                continue
            print(list)
    return print(list)

li = [9,1,6,8,4,3,2,0,5,7]
selection_sort(li)
