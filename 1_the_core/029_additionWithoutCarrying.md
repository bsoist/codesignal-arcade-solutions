Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Addition Without Carrying

A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. But the child always forgets about the important part - carrying.

Given two integers, your task is to find the result that the child will get.

For `param1 = 456` and `param2 = 1734`, the output should be `solution(param1, param2) = 1180`.

## Notes

## Solutions

### Python
```python
def solution(param1, param2):
    total, place = 0, 1
    while param1 > 0 and param2 > 0:
        total += ((param1 + param2) % 10) * place
        place *= 10
        param1 //= 10
        param2 //= 10
    return total
```

### JavaScript
```javascript
function solution(param1, param2) {
    let total = 0, place = 1;
    while (param1 > 0 || param2 > 0) {
        total += (((param1 % 10) + (param2 % 10)) % 10) * place;
        place *= 10;
        param1 = Math.floor(param1 / 10);
        param2 = Math.floor(param2 / 10);
    }
    return total;
}
```

### C
```c
int solution(int param1, int param2) {
    int total = 0, place = 1;
    while (param1 > 0 || param2 > 0) {
        total += (((param1 % 10) + (param2 % 10)) % 10) * place;
        place *= 10;
        param1 /= 10;
        param2 /= 10;
    }
    return total;
}
```