def solution(text):
    words = ['']
    for char in text:
        if char.isalpha():
            words[-1] += char
        else:
            if words[-1]:
                words.append('')
    return sorted(zip(map(len, words), words))[-1][1]