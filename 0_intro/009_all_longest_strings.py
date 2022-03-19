def solution(inputArray):
    strings = {}
    for s in inputArray:
        str_len = len(s)
        if str_len not in strings:
            strings[str_len] = []
        strings[str_len].append(s)
    lengths = sorted(strings.keys(), reverse=True)
    return strings[lengths[0]]