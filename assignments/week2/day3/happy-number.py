def isHappy(self, n: int) -> bool:
    hash_set = set()
    sum = 0
    old_sum = n

    while True:
        for num in str(old_sum):
            sum += int(num)**2
        if sum == 1:
            break
        elif sum in hash_set:
            return False
        else:
            hash_set.add(sum)
            old_sum = sum
            sum = 0
    return True