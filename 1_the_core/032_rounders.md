Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Rounders

We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1). The process stops immediately once there is only one non-zero digit left.

For `n = 15`, the output should be `solution(n) = 20`.

For `n = 1234`, the output should be `solution(n) = 1000`.

`1234 -> 1230 -> 1200 -> 1000`.

For `n = 1445`, the output should be `solution(n) = 2000`.

`1445 -> 1450 -> 1500 -> 2000`.

## Notes

## Solutions

### Python
```python
def solution(n):
    zeros = 0
    inc = False
    while n > 10:
        d = (n % 10) + inc
        inc = d > 4
        n //= 10
        zeros += 1
    return (n + inc) * 10 ** zero
```

### JavaScript
```javascript
function solution(n) {
    let zeros = 0;
    let inc = false;
    while (n > 10) {
        d = (n % 10) + inc;
        inc = d > 4;
        n = Math.floor(n / 10);
        zeros++;
    }
    return (n + inc) * 10 ** zeros;
}
```

### C
```c
int solution(int n) {
    int zeros = 0;
    bool inc = false;
    while (n > 10) {
        int d = (n % 10) + inc;
        inc = d > 4;
        n /= 10;
        zeros++;
    }
    return (n + inc) * pow(10, zeros);
}
```