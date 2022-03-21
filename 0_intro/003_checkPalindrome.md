# Check Palindrome

## Notes
Done this one many times in many languages.

## Solutions

### Python
This is my typical approach in Python. Seems like the simplest approach.
```python
def solution(inputString):
    return inputString == ''.join(reversed(inputString))
```

### JavaScript
Taking the reversing approach seems like too much work in JS and C, which is 
probably reason enough to have not done it that way in Python either. :) 
```javascript
function solution(inputString) {
    for (let i = 0, n = inputString.length, e = Math.floor(n/2); i < e; i++) {
        if (inputString[i] != inputString[n-i-1]) {
            return false;
        }
    }
    return true;
}
```

### C
```c
}bool solution(char * inputString) {
    for (int i = 0, n = strlen(inputString); i < n / 2; i++) {
        if (inputString[i] != inputString[n-i-1]) {
            return false;
        }
    }
    return true;
}
```
