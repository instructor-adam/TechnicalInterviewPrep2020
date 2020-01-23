def dailyTemperaturesNaive(T):
    array = []
    for index in range(0, len(T) - 1):
        for second_index in range(index + 1, len(T)):
            if T[second_index] > T[index]:
                array.append(second_index - index)
                break
            elif second_index == len(T) - 1 and T[second_index] <= T[index]:
                array.append(0)
    
    array.append(0)
    return array


def dailyTemperatures(T):
    array = []

    max = 0
    for index in range(len(T) - 1, -1, -1):
        
        



    return array


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))