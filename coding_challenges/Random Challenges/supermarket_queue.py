# Don's answer

def queue_time(customers, n, tills=None):
    if len(customers) == 0:
        if tills is not None:
            current_max = max(tills.keys(), key=(lambda k: tills[k]))
            return tills[current_max]
        return 0
    if tills is None:
        tills = {i:0 for i in range(n)}
    current_key = min(tills.keys(), key=(lambda k: tills[k]))
    tills[current_key] += customers[0]
    return queue_time(customers[1:], n, tills)