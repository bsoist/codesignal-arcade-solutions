def solution(votes, k):
    to_win = max(votes)
    if k == 0:
        return int(votes.count(to_win) < 2)
    return sum([(vote + k) > to_win for vote in votes]) 
    