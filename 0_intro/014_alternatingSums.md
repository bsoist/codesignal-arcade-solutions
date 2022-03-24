Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Alternating Sums

Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

For `a = [50, 60, 60, 45, 70]`, the output should be `solution(a) = [180, 105]`.

## Notes
It's not clear to me from the given information (perhaps because I'm missing something) whether the array will always have an even number of elements.

## Solutions

### Python
```python
def solution(a):
    weights = [0, 0]
    i = 0
    for weight in a:
        weights[i] += weight
        i = int(not i)
    return weights
```

### JavaScript
```javascript
function solution(a) {
    let weights = [0, 0];
    for (let i = 0; i < a.length; i++) {
        weights[i % 2] += a[i];
    }
    return weights;
}
```

### C

I am realizing now that I am not checking these arr_##type things for NULL. Not sure if that matters or not.

```c
arr_integer solution(arr_integer a) {
    arr_integer weights = alloc_arr_integer(2);
    weights.arr[0] = 0;
    weights.arr[1] = 0;
    for (int i = 0; i < a.size; i++) {
        weights.arr[i % 2] += a.arr[i];
    }        
    return weights;
}
```