# All Longest Strings
Given an array of strings, return another array containing all of its longest strings.

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

## Notes
With less than eleven elements in the list, it seems reasonable to just find the max length and then loop again and print the longest ones.

## Solutions

### Python
In Python, it made sense to me to save the differnet lengths in separate lists, sort them by length, and return the right one.
```python
def solution(inputArray):
    strings = {}
    for s in inputArray:
        str_len = len(s)
        if str_len not in strings:
            strings[str_len] = []
        strings[str_len].append(s)
    lengths = sorted(strings.keys(), reverse=True)
    return strings[lengths[0]]
```

### JavaScript
```javascript
function solution(inputArray) {
    var maxLength = 0;
    inputArray.forEach(function(s) {
        if (s.length > maxLength) {
            maxLength = s.length;
        }
    });
    return inputArray.filter(s => s.length == maxLength);
}
```

### C
I had some trouble figuring out how to use the CodeSignal specific arrays.

```c
arr_string solution(arr_string inputArray) {
    int max_length = 0;
    for (int i = 0; i < inputArray.size; i++) {
        int str_len = strlen(inputArray.arr[i]);
        if (str_len > max_length) {
            max_length = str_len;
        }
    }
    int new_length = 0;
    for (int i = 0; i < inputArray.size; i++) {
        if (strlen(inputArray.arr[i]) == max_length) {
            new_length++;
        }
    }
    arr_string new_strings = alloc_arr_string(new_length);
    int c = 0;
    for (int i = 0; i < inputArray.size; i++) {
        if (strlen(inputArray.arr[i]) == max_length) {
            new_strings.arr[c] = inputArray.arr[i];
            c++;
        }
    }
    return new_strings;
}
```