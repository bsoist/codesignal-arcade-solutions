def solution(score1, score2):
    lose, win = sorted((score1, score2))
    if win < 6: return False
    if win == 6: return lose < 5
    if win == 7: return 4 < lose < 7
    return win == 6