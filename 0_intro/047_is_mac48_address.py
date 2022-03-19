def solution(inputString):
    pattern = '-'.join(
        ['[0-9A-F][0-9A-F]'] * 6
    )
    pattern = '^' + pattern + '$'
    if re.search(pattern, inputString) is None:
        return False
    return len(inputString) == 17