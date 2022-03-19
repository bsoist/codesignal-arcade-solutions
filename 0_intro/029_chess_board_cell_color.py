def solution(cell1, cell2):
    return (
        len(set(((ord(cell1[0])-64) % 2, int(cell1[1]) % 2))) == 
        len(set(((ord(cell2[0])-64) % 2, int(cell2[1]) % 2)))        
    )
     