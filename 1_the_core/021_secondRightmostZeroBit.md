Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Second Rightmost Zero Bit

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.

Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.

Return the value of `2 ^ position_of_the_found_bit`.

For `n = 37`, the output should be `solution(n) = 8`.

`3710 = 1001012`. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.

Thus, the answer is `8 (2^3)`


## Notes
No option to solve this one in C.

## Solutions

### Python
```python
def solution(n):
    return 2 ** (len(''.join(bin(n)[2:].split('0')[-2:])) + 1)
```

### JavaScript

I don't have a lot of motivation to do this in JavaScript.

```javascript
```

### C

No option to sumit this one in C.

```c
```