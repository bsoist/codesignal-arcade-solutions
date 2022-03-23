# Common Character Count
Given two strings, find the number of common characters between them.

## Notes
Another example of something that seems natural to me in Python. Remove an item from one list and try to find and remove it from the other. Count the number of times I succeed.

## Solutions

### Python
```python
def solution(s1, s2):
    count = 0
    s1, s2 = list(s1), list(s2)
    while s1:
        try:
            s2.remove(s1.pop())
        except:
            pass
        else:
            count += 1
    return count
```

### JavaScript
I guess I can take the same approach here.

I'm not sure if it matters, but I'll start with figuring out which string is longer. It might make sense to do the multiple iteration over the smaller one.

```javascript
function solution(s1, s2) {
    var count = 0;
    if (s2.length > s1.length) {
        // switch them
        var temp = s2;
        s2 = s1;
        s1 = temp;
    }
    s2 = s2.split('');
    var index;
    for (let i = 0; i < s1.length; i++) {
        index = s2.indexOf(s1[i]);
        if (index > -1) {
            s2.splice(index, 1);
            count++;
        }
    }
    return count;
}
```

### C
Seems like too much work to remove items when they are matched, so I'll just replace them with a character not valid in the original string.

I'll try first without caring which one is longer.

```c
int solution(char * s1, char * s2) {
    int count = 0;
    for (int i = 0, n = strlen(s1); i < n; i++) {
        for (int j = 0, n = strlen(s2); j < n; j++) {
            if (s2[j] == s1[i]) {
                count++;
                s2[j] = '-';
                break;
            }
        }
    }
    return count;
}
```