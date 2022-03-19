def solution(code):
    return ''.join([
        chr(int(str(code[i:i+8]),2))
        for i in range(0, len(code), 8)
    ])