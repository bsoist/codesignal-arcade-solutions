def solution(bishop, pawn):
    b_file, b_rank = ord(bishop[0])-96, int(bishop[1])
    p_file, p_rank = ord(pawn[0])-96, int(pawn[1])
    return abs(b_file - p_file) == abs(b_rank - p_rank)