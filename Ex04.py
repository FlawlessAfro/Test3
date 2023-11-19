list_of_lists = [1,[2,3,"4"], [5,[6,"7",8],9,10]]

list_of_lists[1].remove("4")
list_of_lists[1].insert(2, 4)

list_of_lists[2][1].remove("7")
list_of_lists[2][1].insert(1, 7)



print(list_of_lists)


