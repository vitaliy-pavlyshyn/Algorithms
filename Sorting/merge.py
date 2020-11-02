from random import randint


# Here we have algorithms with time complexity - O(n log(n))


def merge_sort(inp_list):
    if len(inp_list) <= 1:
        return inp_list
    middle = len(inp_list) // 2
    left_list = inp_list[:middle]
    right_list = inp_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left, right):
    res = []
    left_index = right_index = 0
    left_len, right_len = len(left), len(right)
    for _ in range(left_len + right_len):
        if left_index < left_len and right_index < right_len:
            if left[left_index] <= right[right_index]:
                res.append(left[left_index])
                left_index += 1
            else:
                res.append(right[right_index])
                right_index += 1
        elif left_index == left_len:
            res.append(right[right_index])
            right_index += 1
        elif right_index == right_len:
            res.append(left[left_index])
            left_index += 1
    return res


a = [randint(1, 100) for i in range(10)]
print(a)
a = merge_sort(a)
print(a)
