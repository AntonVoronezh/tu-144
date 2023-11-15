
def make_uniq_arr(arr):
    new_arr = []

    for elem in arr:
        if elem not in new_arr:
            new_arr.append(elem)

    return new_arr