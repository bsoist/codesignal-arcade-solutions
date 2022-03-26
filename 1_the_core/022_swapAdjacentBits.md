Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Swap Adjacent Bits
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.

You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. Then return the result as a decimal number.

* For `n = 13`, the output should be `solution(n) = 14`. 
    `13 = 1101 ~> {11}{01} ~> 1110 = 14`.

* For n = 74, the output should be `solution(n) = 133`.
    `74 = 01001010 ~> {01}{00}{10}{10} ~> 10000101 = 133`.

    Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have 32 bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.

## Notes

Another one of these "do it in one line" tasks. No option to submit in C.

It did not occur to me to try simple bit-shifting until I came up with the mess below. :) 

1101
1010
1001

1101
0101
0101

## Solutions

### Python
```python
def solution(n):
    return int(''.join([''.join(p) for p in reversed(list(zip(
            ('0'+bin(n)[2:])[::-2],
            ('0'+bin(n)[2:])[:-1][::-2]
        )))]), 2)
```

### JavaScript
```javascript
```

### C
```c
```