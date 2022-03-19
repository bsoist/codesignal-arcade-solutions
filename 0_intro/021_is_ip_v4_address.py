def solution(inputString):
    parts = inputString.split('.')
    if len(parts) != 4: return False
    for part in parts:
        try:
            num = int(part)
        except ValueError:
            return False
        if '0' in part and num != 0:
            return False
        if num == 0 and len(part) > 1:
            return False
        if not (-1 < num < 256):
            return False
    return True