def getTimes(time, direction):
    final_times = [0 for _ in time]
    exit_list = []
    enter_list = []
    for index, value in enumerate(direction):
        if value == 1:
            exit_list.append(index)
        else:
            enter_list.append(index)
    enter_index = 0
    exit_index = 0
    enter_length = len(enter_list)
    exit_length = len(exit_list)
    last_time = -1
    last_direction = -1
    while (enter_index < enter_length) and (exit_index < exit_length):
        exit_time = time[exit_list[exit_index]]
        enter_time = time[enter_list[enter_index]]
        if exit_time <= last_time:
            exit_time = last_time + 1
        if enter_time <= last_time:
            enter_time = last_time + 1
        print(enter_time, exit_time, last_time)
        if enter_time < exit_time:
            final_times[enter_list[enter_index]] = enter_time
            last_time = enter_time
            last_direction = 0
            enter_index += 1
        elif exit_time < enter_time:
            final_times[exit_list[exit_index]] = exit_time
            last_time = exit_time
            last_direction = 1
            exit_index += 1
        elif ((enter_time - 1) == last_time) and (last_direction == 0):
            final_times[enter_list[enter_index]] = enter_time
            last_time = enter_time
            last_direction = 0
            enter_index += 1
        else:
            final_times[exit_list[exit_index]] = exit_time
            last_time = exit_time
            last_direction = 1
            exit_index += 1
    while (exit_index < exit_length):
        exit_time = time[exit_list[exit_index]]
        if exit_time <= last_time:
            exit_time = last_time + 1
        last_time = exit_time
        final_times[exit_list[exit_index]] = exit_time
        exit_index += 1
    while (enter_index < enter_length):
        enter_time = time[enter_list[enter_index]]
        if enter_time <= last_time:
            enter_time = last_time + 1
        last_time = enter_time
        final_times[enter_list[enter_index]] = enter_time
        enter_index += 1
    return final_times
