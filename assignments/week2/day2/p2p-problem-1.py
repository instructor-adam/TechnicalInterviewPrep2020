# O(1) Space | O(N * N) Time
def replaceElementsNaive(arr):
    for num in range(0, len(arr)):
        if num == len(arr) - 1:
            arr[-1] = -1
            break

        max_num = arr[num + 1]
        for next_num in range(num + 1, len(arr)):
            print(next_num)
            if arr[next_num] > max_num:
                max_num = arr[next_num]
        arr[num] = max_num
    return arr


# O(1) Space | O(N) Time
def replaceElements(arr):
    max_num = arr[-1]
    arr[-1] = -1
    for num in range(len(arr) - 2, -1, -1):
        if arr[num] > max_num:
            temp = arr[num]
            arr[num] = max_num
            max_num = temp
        else:
            arr[num] = max_num
    return arr
