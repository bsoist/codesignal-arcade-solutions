Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Count Sum of Two Representations 2

Given integers `n`, `l` and `r`, find the number of ways to represent `n` as a sum of two integers `A` and `B` such that `l ≤ A ≤ B ≤ r`.

Example

For `n = 6`, `l = 2`, and `r = 4`, the output should be `solution(n, l, r) = 2`.

There are just two ways to write `6` as `A + B`, where `2 ≤ A ≤ B ≤ 4`: `6 = 2 + 4` and `6 = 3 + 3`.

## Notes

So, `A ≤ B` and both must be within `l` and `r` inclusive.

~~There is no mention of this not being possible, so I think I can assume if `l == r` that there is only one pair `l + r` but I haven't tested that assumption yet.~~ WRONG

The constraints might be helpful for this one.

`5 ≤ n ≤ 109`
`1 ≤ l ≤ r`
`l ≤ r ≤ 109`
`r - l ≤ 106`

## Solutions

### Python
```python
def solution(n, l, r):
    if l == r: return 1
    pairs = 0
    while l <= r:
        if l <= l <= (n - l) <= r:
            pairs += 1
        l += 1
    return pairs
```


### JavaScript
```javascript
```

### C
```c
```