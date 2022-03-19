def solution(inputArray):
    last_obstacle = max(inputArray)
    obstacles = set(inputArray)
    def walk(gap):
        spot = gap
        while True:
            if spot > last_obstacle:
                return True
            if spot in obstacles:
                return False
            spot += gap
        
    for i in range(1,last_obstacle+2):
        if walk(i):
            return i

def solution(inputArray):
    last_obstacle = max(inputArray)
    obstacles = set(inputArray)
    def walk(gap):
        spot = gap
        while True:
            if spot > last_obstacle:
                return True
            if spot in obstacles:
                return False
            spot += gap
        
    for i in range(1,last_obstacle+2):
        if walk(i):
            return i

