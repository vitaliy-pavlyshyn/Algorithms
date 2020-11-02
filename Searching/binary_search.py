def division(num1, num2):
    if num1 == 0: return 0
    if num2 == 0: return INT_MAX
    negative_result = 0
    if num1 < 0:
        num1 = - num1
        if num2 < 0:
            num2 = - num2
        else:
            negative_result = True
    elif num2 < 0:
        num2 = - num2
        negative_result = True

    quotient = 0

    while num1 >= num2:
        num1 = num1 - num2
        quotient += 1
    if negative_result:
        quotient -= quotient
    return quotient


def binary_search(lis, left_index, right_index, x):
    if right_index >= left_index:
        p = (right_index - left_index)
        mid = left_index + half(p)
        if lis[mid] == x:
            return mid
        elif lis[mid] > x:
            return binary_search(lis, left_index, mid - 1, x)
        else:
            return binary_search(lis, mid + 1, right_index, x)
    else:
        return -1


a = [i for i in range(1000)]

print(binary_search(a, 0, len(a) - 1, 9))
