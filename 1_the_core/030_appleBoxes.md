Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Apple Boxes

You have `k` apple boxes full of apples. Each square box of size `m` contains `m × m` apples. You just noticed two interesting properties about the boxes:

The smallest box is size `1`, the next one is size `2`,..., all the way up to size `k`.

Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.

Your task is to calculate the difference between the number of red apples and the number of yellow apples.

For `k = 5`, the output should be `solution(k) = -15`.

There are `1 + 3 * 3 + 5 * 5 = 35` yellow apples and `2 * 2 + 4 * 4 = 20` red apples, making the answer `20 - 35 = -15`.

## Notes

I could just add or subtract based on whether it's odd or even, or save in a difrent slot and subtract after.

## Solutions

### Python
```python
def solution(k):
    m, total = -1, 0
    for i in range(1,k + 1):
        total += i**2 * m
        m *= -1 
    return total

def solution(k):
    totals = [0, 0]
    for i in range(1,k + 1):
        totals[i % 2] = i**2
    return totals[0] - totals[1]
```

### JavaScript
```javascript
```

### C
```c
```