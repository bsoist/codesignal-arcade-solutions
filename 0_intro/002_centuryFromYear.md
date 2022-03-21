# Century From Year
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

## Notes
Simplest way I can think of is to just mod off the ones digit.

## Solutions

### Python
```python
def solution(year):
    return ((year - 1) // 100) + 1
```

### JavaScript
```javascript
function solution(year) {
    return Math.floor((year - 1) / 100) + 1;
}
```

### C
```c
int solution(int year) {
    return ((year - 1) / 100) + 1;
}
```

