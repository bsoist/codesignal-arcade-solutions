def solution(s):
    output = [s[0]]
    for char in s[1:] + '0':
        if char == output[-1][0]:
            output[-1] += char
        else:
            enc = output[-1][0]
            num = len(output[-1])
            if num > 1:
                enc = f'{num}{enc}'
            output[-1] = enc
            if char != '0':
                output.append(char)
    return ''.join(output)