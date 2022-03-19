def solution(inputString):
    from collections import defaultdict, Counter
    counts = defaultdict(int)
    counts.update(Counter(inputString))
    prev_count = counts['a']
    for letter in string.ascii_lowercase[1:]:
        if counts[letter] > prev_count: return False
        prev_count = counts[letter]
    return True