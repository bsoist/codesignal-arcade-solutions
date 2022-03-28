Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Equal Pair of Bits

You're given two integers, `n` and `m`. Find position of the rightmost pair of equal bits in their binary representations (it is guaranteed that such a pair exists), counting from right to left.

Return the value of `2^position_of_the_found_pair` (0-based).

For `n = 10` and `m = 11`, the output should be `solution(n, m) = 2`.

`10 = 1010, 11 = 1011`, the position of the rightmost pair of equal bits is the bit at position `1` (0-based) from the right in the binary representations.

So the answer is `2^1 = 2`.

## Notes

Another one-liner.

The important thing here is that Python stores negative integers as the complement of the preceding number. In other words, -7 is stored as the complement of 6.

The binary representation of `10` is `1010`. The binary representation of `11` is `1011`. Performing and `XOR` gives `0001` and the complement of that is `1110` which tells us which bits are the same (the 1s). The key now is to grab only the rigth-most so we have `0010` which we could get by doing an `AND` with `0010` or the complement of `1101`. Note that `1101` is one less than `1110`. All of this give us...

`~(n ^ m) & -(~(n ^ m))`



## Solutions

### Python
```python
def solution(n, m):
    return ~(n ^ m) & -(~(n ^ m))
```

### JavaScript
```javascript
function solution(n, m) {
  return ~(n ^ m) & -(~(n ^ m));
}
```

### C
```c
```