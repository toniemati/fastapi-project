def quicksort(arr, key, order="asc"):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    if order == "asc":
        left = [x for x in arr if getattr(x, key) < getattr(pivot, key)]
        middle = [x for x in arr if getattr(x, key) == getattr(pivot, key)]
        right = [x for x in arr if getattr(x, key) > getattr(pivot, key)]
    else:
        left = [x for x in arr if getattr(x, key) > getattr(pivot, key)]
        middle = [x for x in arr if getattr(x, key) == getattr(pivot, key)]
        right = [x for x in arr if getattr(x, key) < getattr(pivot, key)]

    return quicksort(left, key, order) + middle + quicksort(right, key, order)
