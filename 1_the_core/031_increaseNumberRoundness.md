Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Increase Number Roundness

Define an integer's roundness as the number of trailing zeroes in it.

Given an integer `n`, check if it's possible to increase `n`'s roundness by swapping some pair of its digits.

For `n = 902200100`, the output should be `solution(n) = true`.

One of the possible ways to increase roundness of `n` is to swap digit `1` with digit `0` preceding it: roundness of `902201000` is `3`, and roundness of `n` is `2`.

For instance, one may swap the leftmost `0` with `1`.

For `n = 11000`, the output should be `solution(n) = false`.

Roundness of `n` is `3`, and there is no way to increase it.

## Notes

## Solutions

### Python
```python
def solution(n):
    return len([i for i in str(n).split('0') if i]) > 1
```

### JavaScript
```javascript
function solution(n) {
    let non_zero_found = false;
    while (n > 0) {        
        let last_digit = n % 10;
        if (last_digit != 0) {
            non_zero_found = true;
        } else {
            if (non_zero_found) {
                return true;
            }            
        }
        n = Math.floor(n / 10);
    }
    return false;
}
```

### C
```c
bool solution(int n) {
    bool non_zero_found = false;
    while (n > 0) {        
        int last_digit = n % 10;
        if (last_digit != 0) {
            non_zero_found = true;
        } else {
            if (non_zero_found) {
                return true;
            }            
        }
        n /= 10;
    }
    return false;
}

```