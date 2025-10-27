def frequencies(list):
    if len(list) == 0:
        return []
    list = [str(x)for x in list]
    list.sort()
    i = 0
    element = list[0]
    counter = 1
    my_dictionary = {}
    for j in range(1, len(list)):
        if list[j] == list[i]:
            counter += 1
        else:
            my_dictionary[element] = counter
            i = j
            element = list[i]
            counter = 1
    
    my_dictionary[element] = counter
    return my_dictionary

list1 = ['a','a','c','a','b','c']
list2 = [100, 'Hello', '100', '100', 100]

print(frequencies(list1))
print(frequencies(list2))
