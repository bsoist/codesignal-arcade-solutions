Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Create Array

Given an integer `size`, return array of length `size` filled with `1`s.

For `size = 4`, the output should be `solution(size) = [1, 1, 1, 1]`.

## Notes

## Solutions

### Python
```python
def solution(size):
    return [1] * size
```

### JavaScript
```javascript
function solution(size) {
    return Array(size).fill(1);
}
```

### C
```c
arr_integer solution(int size) {
    arr_integer a = alloc_arr_integer(size);
    for (int i = 0; i < size; i++) {
        a.arr[i] = 1;
    }
    return a;
}
```