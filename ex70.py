# Multitasking (jobs and cooldown):
def findTime(tasks, cooldown):
    lastPosition = {}  # creation of the hashmap
    current = 0

    for task in tasks:
        if task in lastPosition:
            if current - lastPosition[task] <= cooldown:
                # add cooldown
                current = cooldown + lastPosition[task] + 1
            lastPosition[task] = current
            print(lastPosition)   # visualize what happens in the hashmap (can be removed).
        current = current + 1     # advance in the hashmap after comparing cooldown and lastPosition
    return current + 1


print(findTime([1, 1, 2, 1], 2))