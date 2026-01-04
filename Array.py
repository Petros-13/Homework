def array_length_recursive(lst):
    if lst == []:
        return 0
    return 1 + array_length_recursive(lst[1:])

arr = [1, 2, 3, 4, 5]
print(array_length_recursive(arr))
