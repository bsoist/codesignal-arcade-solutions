def solution(name):
    if name[0].isdigit(): return False
    valid_chars = set(string.ascii_letters + string.digits + '_')
    return not bool(len(set(name) - valid_chars))