def solution(inputString):
    output = ''
    for char in inputString:
        output += chr((ord(char) - 97 + 1) % 26 + 97)
    return output