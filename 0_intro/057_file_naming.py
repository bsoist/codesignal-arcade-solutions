def solution(names):
    used = set()
    files = []
    for name in names:
        i, test_name = 0, name
        while test_name in used:
            i += 1
            test_name = f'{name}({i})'
        files.append(test_name)
        used.add(test_name)
    return files