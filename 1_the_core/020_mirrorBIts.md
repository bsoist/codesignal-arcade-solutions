Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Mirror Bits

Reverse the order of the bits in a given integer.

Example

For `a = 97`, the output should be `solution(a) = 67`.

97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

For `a = 8`, the output should be `solution(a) = 1`.

## Notes
Trying to think this trough. Is there some pattern of bits I could use? 

I could get the bits as a string, reverse it, and then convert back, but I'd like to do without converting to strings.

I was going to solve this one in C first, but I want to test my idea more quickly, so I'll start with Python. Maybe something like this...

```python
bin_digits = []
while a > 0:
    bin_digits.append(n % 2)
    a //= 2
# then some way to convert it back
```

## Solutions

### Python
```python
def solution(a):
    bin_digits = ''
    while a > 0:
        bin_digits += str(a % 2)
        a //= 2
    return int(bin_digits, 2)
```

### JavaScript
```javascript
function solution(a) {
    let bin_digits = [];
    while (a > 0) {
        bin_digits.push(a % 2);
        a = Math.floor(a / 2);
    }
    let answer = 0;
    for (let i = 0; i < bin_digits.length; i++) {
        answer += (2 * bin_digits[i]) ** (bin_digits.length - 1 - i);
    }
    return answer;
}
```

### C

After the while loop,  `i` will equal the length of the useful digits.

```c
int solution(int a) {
    int bin_digits[17];
    int i = 0;
    while (a > 0) {
        bin_digits[i] = a % 2;
        a /= 2;
        i++;
    }
    int num_digits = i; // save this
    int answer = 0;
    for (int i = 0; i < num_digits; i++) {
        answer += pow(2 * bin_digits[i], num_digits - 1 - i);
    }
    return answer;
}
```