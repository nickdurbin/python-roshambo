def arrayMedian(sequence):
    sequence.sort()
    sum = 0
    n = int(len(sequence) / 2)
    if len(sequence) % 2 != 0:
        median = sequence[n]
        return median
    else:
        sum = sequence[n - 1] + sequence[n]
        median = sum/2
        return median