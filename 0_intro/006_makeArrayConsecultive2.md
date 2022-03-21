# Make Array Consecutive 2
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

## Notes
Less than 11 elements in the array so iterating over it several times doesn't seem unreasonable. So, we can just use min and max functions.

I'll go ahead and do it the "right way" in the C solution.

## Solutions

### Python
```python
def solution(statues):
    return (
        max(statues) - min(statues)
    ) - len(statues) + 1
```

### JavaScript
```javascript
function solution(statues) {
    return (Math.max(...statues) - Math.min(...statues)) - statues.length + 1;
}
```

### C
```c
int solution(arr_integer statues) {
    int min = 21; // gaurantted constraint
    int max = -1; // gaurantted constraint
    for (int i = 0; i < statues.size; i++) {
        if (statues.arr[i] < min) {
            min = statues.arr[i];
        }
        if (statues.arr[i] > max) {
            max = statues.arr[i];
        }
    }
    return max - min - statues.size + 1;
}
```