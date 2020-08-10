

def binary_search(item, ls):
    low = 0
    high = len(ls) -1

    while low <= high:
        middle = (low + high) // 2
        guess = ls[middle]

        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1

    return None



ls = [1,3,5,7,9]
print(binary_search(7,ls))
print(binary_search(12,ls))