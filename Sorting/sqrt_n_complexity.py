# Here we have sort algorithms with complexity O(n^2)


def bubble_sort(lis):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lis) - 1):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                swapped = True
    return lis


def selection_sort(lis):
    for i in range(len(lis)):  # Numbers of swaps
        minimum_item_index = i  # Assume that first element is the smallest
        for x in range(i + 1, len(lis)):  # Iterate over 'unsorted list'
            if lis[x] < lis[minimum_item_index]:
                minimum_item_index = x
        lis[i], lis[minimum_item_index] = lis[minimum_item_index], lis[i]
    return lis


def insertion_sort(lis):
    for i in range(1, len(lis)):
        item_to_insert = lis[i]  # Copy inserting item
        previous_item_index = i - 1
        while previous_item_index >= 0 and lis[previous_item_index] > item_to_insert:
            lis[previous_item_index + 1] = lis[previous_item_index]
            previous_item_index -= 1
        lis[previous_item_index + 1] = item_to_insert
    return lis
