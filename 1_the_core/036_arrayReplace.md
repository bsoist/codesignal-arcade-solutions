Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Array Replace

## Notes

## Solutions

### Python
```python
def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if elem == 
            elemToReplace else elem 
            for elem in inputArray
```

### JavaScript
```javascript
function solution(inputArray, elemToReplace, substitutionElem) {
    for (let i = 0; i < inputArray.length; i++) {
        if (inputArray[i] == elemToReplace) {
            inputArray[i] = substitutionElem;
        }
    }
    return inputArray;
}
```

### C
```c
arr_integer solution(arr_integer inputArray, int elemToReplace, int substitutionElem) {
    for (int i = 0; i < inputArray.size; i++) {
        if (inputArray.arr[i] == elemToReplace) {
            inputArray.arr[i] = substitutionElem;
        }
    }
    return inputArray;
}
```