def solution(sequence):
    seq_len = len(sequence)
    if seq_len < 3: return True
    if seq_len - len(set(sequence)) > 1: return False
    a, b = min(sequence[:3]), max(sequence[:3])    
    if sequence[0] < sequence[1]:
        nums = sequence[:2]
        removed = False
        if sequence[2] > sequence[1]:
            nums.append(sequence[2])
        else:
            removed = True
    elif sequence[1] < sequence[2]:
        nums = sequence[1:3]
        removed = True
    else:
        if seq_len == 3: return False
        
    for i in range(3, len(sequence)):
        if sequence[i] > nums[-1]:
            nums.append(sequence[i])
        elif removed:
            return False
        else:
            nums.pop()
            removed = True
    return sequence[-1] != sequence[-2]