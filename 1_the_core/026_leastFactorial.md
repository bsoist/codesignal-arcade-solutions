Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Least Factorial

Given an integer `n`, find the minimal `k` such that

        * `k = m!` (where `m! = 1 * 2 * ... * m`) for some integer `m`;
        * `k >= n`.

In other words, find the smallest factorial which is not less than `n`.

Example

For `n = 17`, the output should be `solution(n) = 24`.

`17 < 24 = 4! = 1 * 2 * 3 * 4`, while `3! = 1 * 2 * 3 = 6 < 17`.

## Notes

Should be able to just keep multiplying and then return when we've gone over.

## Solutions

### Python
```python
def solution(n):
    if n < 3: return n
    f, answer = 4, 6
    while answer < n:
        answer *= f
        f += 1
    return answer 
```

### JavaScript
```javascript
function solution(n) { 
    if (n < 3) return n;
    let f = 4, answer = 6;
    while (answer < n) {
        answer *= f
        f++;
    }
    return answer 
}
```

### C

Almost exactly the same at the JavaScript.

```c
int solution(int n) {
    if (n < 3) return n;
    int f = 4, answer = 6;
    while (answer < n) {
        answer *= f;
        f++;
    }
    return answer;
}
```