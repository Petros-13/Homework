def max_difference(arr):
    if len(arr) < 2:
        return 0

    min_val = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_val)
        min_val = min(min_val, arr[i])

    return max_diff


a = [4, 5, 234, 2, 6, 82, 234, 5234]
print(max_difference(a))
