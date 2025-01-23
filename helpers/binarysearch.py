def binary_search(products, name):
    left, right = 0, len(products) - 1

    while left <= right:
        mid = (left + right) // 2

        if name.lower() in products[mid].name.lower():
            return products[mid]
        elif name.lower() < products[mid].name.lower():
            right = mid - 1
        else:
            left = mid + 1

    return None
