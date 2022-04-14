Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Count Black Cells

Imagine a white rectangular grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:

A cell is painted black if it has at least one point in common with the diagonal; Otherwise, a cell is painted white.

Count the number of cells painted black.

## Notes

## Solutions

### Python
```python
def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)

def solution(n, m):
    if n == m: return n + 2 * (n - 1)
    if 1 in {n, m}: return n * m
    return n + m - gcd(n, m) + (gcd(n, m) - 1) * 2

```

### JavaScript
```javascript
function gcd(a, b) {
    if (a == 0) return b;
    if (b == 0) return a;
    if (a > b) {
        return gcd(a % b, b);
    } else {
        return gcd(a, b % a);
    }
}

function solution(n, m) {
    if (n == m) return n + 2 * (n - 1);
    if (n == 1 || m == 1) return n * m;
    return n + m - gcd(n, m) + (gcd(n, m) - 1) * 2;
}
```

### C
```c
int gcd(int a, int b) {
    if (a == 0) return b;
    if (b == 0) return a;
    if (a > b) {
        return gcd(a % b, b);
    } else {
        return gcd(a, b % a);
    }
}
int solution(int n, int m) {
    if (n == m) return n + 2 * (n - 1);
    if (n == 1 || m == 1) return n * m;
    return n + m - gcd(n, m) + (gcd(n, m) - 1) * 2;
}
```