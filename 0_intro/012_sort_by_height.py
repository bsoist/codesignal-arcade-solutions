def solution(a):
    i = 0
    sorted_heights = []
    for height in sorted(a):
        if height != -1:
            while a[i] == -1:
                i += 1
            a[i] = height
            i += 1
    return a