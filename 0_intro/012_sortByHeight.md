# Sort by Height
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

For `a = [-1, 150, 190, 170, -1, -1, 160, 180]`, the output should be
`solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190]`.

## Notes
If I make a sorted copy, it will have all the trees at the beginning. Then I can iterate through the sorted version and if I find a person, I can proceed through the unsorted until I find the next non-tree and replace that height.

## Solutions
Pretty easy to do in Python using [Timsort](https://en.wikipedia.org/wiki/Timsort)

Should work pretty well with standard sort too, so I'll try it in JavaScript and C.

### Python
```python
def solution(a):
    i = 0
    sorted_heights = []
    for height in sorted(a):
        if height != -1:
            while a[i] == -1:
                i += 1
            a[i] = height
            i += 1
    return a
```

### JavaScript
```javascript
function solution(a) {
    sortedCopy = [...a];
    sortedCopy.sort((x, y) => x - y);
    let i = 0;
    let sortedHeights = [];
    sortedCopy.forEach((height) => {
        if (height != -1) {
            while (a[i] == -1) {
                i += 1;
            }
            a[i] = height;
            i += 1;
        }
    });
    return a;
}
```

### C
```c
arr_integer solution(arr_integer a) {
    int compare( const void* a, const void* b)
    {
        if ( *(int*)a <  *(int*)b ) return -1;
        if ( *(int*)a == *(int*)b ) return 0;
        if ( *(int*)a >  *(int*)b ) return 1;
    }

    // make a copy
    int sorted_heights[a.size];
    for (int i = 0; i < a.size; i++) {
        sorted_heights[i] = a.arr[i];
    }

    // sort the copy
    qsort(sorted_heights, a.size, sizeof(int), compare);
    int i = 0;
    for (int j = 0; j < a.size; j++) {
        int height = sorted_heights[j];
        if (height != -1) {
            while (a.arr[i] == -1) {
                i += 1;
            }
            a.arr[i] = height;
            i += 1;
        }
    }
    return a;
}
```
