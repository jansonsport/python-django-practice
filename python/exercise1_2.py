def median(list):
    list.sort()
    med_index = int(len(list)/2)
    if len(list) % 2 == 0:
        a = list[med_index -1]
        b = list[med_index]
        #print(a)
        #print(b)
        print(float((a+b)/2))
    else:
        print(float(list[med_index]))

list1 = [1,2,3,4,5]
list2 = [8, 789, 2, 9, 391]
list3 = [6,7,9,4658,2365,1,1,1]
#[1,1,1,6,7,9,2365,4658]
list4 = [2,2,2,9,9,9,9,2,2,2]
list5 = [3]

median(list1)
median(list2)
median(list3)
median(list4)
median(list5)

#test
