Be sure to [attempt this problem](https://github.com/bsoist/codesignal-arcade-solutions) on your own before looking at the solutiosn below.

# Add Border

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

For

```
picture = ["abc",
           "ded"]
```

the output should be

```
solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
```

## Notes

The strings are guaranteed to be equal length.

## Solutions

### Python
```python
def solution(picture):
    bordered = ['*' * (len(picture[0]) + 2)]
    for row in picture:
        bordered.append('*' + row + '*')
    bordered.append(bordered[0])
    return bordered
```

### JavaScript
```javascript
function solution(picture) {
    let bordered = ['*'.repeat(picture[0].length + 2)]
    for (let i = 0; i < picture.length; i++) {
        bordered.push('*' + picture[i] + '*');
    }
    bordered.push(bordered[0]);
    return bordered;
}
```

### C

I'm not thrilled with this one, but it works.

```c
arr_string solution(arr_string picture) {
    arr_string bordered = alloc_arr_string(picture.size + 2);
    int width = strlen(picture.arr[0]) + 2;
    bordered.arr[0] = (char*) malloc(sizeof(char) * (width + 1));
    memset(bordered.arr[0], '*', width);
    int i;
    for (i = 0; i < picture.size; i++) {
        bordered.arr[i + 1] = (char*) malloc(sizeof(char) * (width + 1));
        strcat(bordered.arr[i + 1], "*");
        strcat(bordered.arr[i + 1], picture.arr[i]);
        strcat(bordered.arr[i + 1], "*");
    }
    bordered.arr[i + 1] = (char*) malloc(sizeof(char) * (width + 1));
    memset(bordered.arr[i + 1], '*', width);
    printf("%i %i\n", picture.size, i);
    return bordered;
}
```