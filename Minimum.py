def minimum_flips(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    return min(count_0, count_1)

arr = [1, 0, 1, 1, 0]
print(minimum_flips(arr))
