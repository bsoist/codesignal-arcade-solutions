Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Different Rightmost Bit

You're given two integers, n and m. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.

Return the value of `2 ^ position_of_the_found_bit` (0-based).

Example

For `n = 11` and `m = 13`, the output should be `solution(n, m) = 2`.

11 = 1011, 13 = 1101, the rightmost bit in which they differ is the bit at position 1 (0-based) from the right in the binary representations. So the answer is `2^1 = 2`.

For `n = 7` and `m = 23`, the output should be `solution(n, m) = 16`.

`7 = 111, 23 = 10111`, i.e.

`00111`
`10111`
So the answer is `2^4 = 16`.

## Notes
Another one-liner

I don't have a lot of experience with bit manipulation, but I did come up with one working solution by experimenting with it.

I also wrote another solution which didn't require it, but it's a long way around, for sure (especially in one line).

## Solutions

### Python

One...

```python
def solution(n, m):
    return (n ^ m) & -(n ^ m)
```

Two...

```python
def solution(n, m):
    return 2 ** [item for item in 
                [i if (p[0] != p[1]) else None 
                for i, p in enumerate(
                            zip(
                                reversed(bin(n)[2:].zfill(len(bin(m)))),
                                reversed(bin(m)[2:].zfill(len(bin(n))))
                                )
                )] if item is not None][0]
```


### JavaScript
```javascript
function solution(n, m) {
  return (n ^ m) & -(n ^ m);
}
```

### C

No option to do submit this in C.