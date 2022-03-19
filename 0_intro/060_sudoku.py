def solution(grid):
    boxes = []
    for i, row in enumerate(grid):
        if len(set(row)) != 9: return False
        if not i % 3:
            boxes.extend([[],[],[]])
        for j in range(3):
            boxes[j-3].extend(row[j*3:j*3+3])
    for box in boxes:
        if len(set(box)) != 9: return False
    for row in zip(*grid):
        if len(set(row)) != 9: return False
    return True